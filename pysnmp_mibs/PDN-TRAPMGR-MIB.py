_I='pdnDevTrapMgrSubnetMask'
_H='pdnDevTrapMgrDestAddress'
_G='devTrapMgrIpAddress'
_F='DisplayString'
_E='Integer32'
_D='PDN-TRAPMGR-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_traps,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-traps')
SwitchState,=mibBuilder.importSymbols('PDN-TC','SwitchState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
_DevTrapMgrMaxNumber_Type=Integer32
_DevTrapMgrMaxNumber_Object=MibScalar
devTrapMgrMaxNumber=_DevTrapMgrMaxNumber_Object((1,3,6,1,4,1,1795,2,24,2,9,1),_DevTrapMgrMaxNumber_Type())
devTrapMgrMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrapMgrMaxNumber.setStatus(_A)
_DevTrapMgrCurrentNumber_Type=Integer32
_DevTrapMgrCurrentNumber_Object=MibScalar
devTrapMgrCurrentNumber=_DevTrapMgrCurrentNumber_Object((1,3,6,1,4,1,1795,2,24,2,9,2),_DevTrapMgrCurrentNumber_Type())
devTrapMgrCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:devTrapMgrCurrentNumber.setStatus(_A)
_DevTrapMgrTable_Object=MibTable
devTrapMgrTable=_DevTrapMgrTable_Object((1,3,6,1,4,1,1795,2,24,2,9,3))
if mibBuilder.loadTexts:devTrapMgrTable.setStatus(_A)
_DevTrapMgrEntry_Object=MibTableRow
devTrapMgrEntry=_DevTrapMgrEntry_Object((1,3,6,1,4,1,1795,2,24,2,9,3,1))
devTrapMgrEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:devTrapMgrEntry.setStatus(_A)
_DevTrapMgrIpAddress_Type=IpAddress
_DevTrapMgrIpAddress_Object=MibTableColumn
devTrapMgrIpAddress=_DevTrapMgrIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,9,3,1,1),_DevTrapMgrIpAddress_Type())
devTrapMgrIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:devTrapMgrIpAddress.setStatus(_A)
_DevTrapMgrDestination_Type=Integer32
_DevTrapMgrDestination_Object=MibTableColumn
devTrapMgrDestination=_DevTrapMgrDestination_Object((1,3,6,1,4,1,1795,2,24,2,9,3,1,2),_DevTrapMgrDestination_Type())
devTrapMgrDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:devTrapMgrDestination.setStatus(_A)
_DevTrapMgrCircuit_Type=Integer32
_DevTrapMgrCircuit_Object=MibTableColumn
devTrapMgrCircuit=_DevTrapMgrCircuit_Object((1,3,6,1,4,1,1795,2,24,2,9,3,1,3),_DevTrapMgrCircuit_Type())
devTrapMgrCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:devTrapMgrCircuit.setStatus(_A)
_DevTrapMgrSubCircuit_Type=Integer32
_DevTrapMgrSubCircuit_Object=MibTableColumn
devTrapMgrSubCircuit=_DevTrapMgrSubCircuit_Object((1,3,6,1,4,1,1795,2,24,2,9,3,1,4),_DevTrapMgrSubCircuit_Type())
devTrapMgrSubCircuit.setMaxAccess(_B)
if mibBuilder.loadTexts:devTrapMgrSubCircuit.setStatus(_A)
_PdnDevTrapMgrTable_Object=MibTable
pdnDevTrapMgrTable=_PdnDevTrapMgrTable_Object((1,3,6,1,4,1,1795,2,24,2,9,4))
if mibBuilder.loadTexts:pdnDevTrapMgrTable.setStatus(_A)
_PdnDevTrapMgrEntry_Object=MibTableRow
pdnDevTrapMgrEntry=_PdnDevTrapMgrEntry_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1))
pdnDevTrapMgrEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:pdnDevTrapMgrEntry.setStatus(_A)
_PdnDevTrapMgrDestAddress_Type=IpAddress
_PdnDevTrapMgrDestAddress_Object=MibTableColumn
pdnDevTrapMgrDestAddress=_PdnDevTrapMgrDestAddress_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,1),_PdnDevTrapMgrDestAddress_Type())
pdnDevTrapMgrDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevTrapMgrDestAddress.setStatus(_A)
_PdnDevTrapMgrSubnetMask_Type=IpAddress
_PdnDevTrapMgrSubnetMask_Object=MibTableColumn
pdnDevTrapMgrSubnetMask=_PdnDevTrapMgrSubnetMask_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,2),_PdnDevTrapMgrSubnetMask_Type())
pdnDevTrapMgrSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevTrapMgrSubnetMask.setStatus(_A)
class _PdnDevTrapMgrDestPort_Type(Integer32):defaultValue=162
_PdnDevTrapMgrDestPort_Type.__name__=_E
_PdnDevTrapMgrDestPort_Object=MibTableColumn
pdnDevTrapMgrDestPort=_PdnDevTrapMgrDestPort_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,3),_PdnDevTrapMgrDestPort_Type())
pdnDevTrapMgrDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDevTrapMgrDestPort.setStatus(_A)
class _PdnDevTrapMgrCommunityName_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_PdnDevTrapMgrCommunityName_Type.__name__=_F
_PdnDevTrapMgrCommunityName_Object=MibTableColumn
pdnDevTrapMgrCommunityName=_PdnDevTrapMgrCommunityName_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,4),_PdnDevTrapMgrCommunityName_Type())
pdnDevTrapMgrCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDevTrapMgrCommunityName.setStatus(_A)
class _PdnDevTrapMgrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_PdnDevTrapMgrEnable_Type.__name__=_E
_PdnDevTrapMgrEnable_Object=MibTableColumn
pdnDevTrapMgrEnable=_PdnDevTrapMgrEnable_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,5),_PdnDevTrapMgrEnable_Type())
pdnDevTrapMgrEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDevTrapMgrEnable.setStatus(_A)
_PdnDevTrapMgrRowStatus_Type=RowStatus
_PdnDevTrapMgrRowStatus_Object=MibTableColumn
pdnDevTrapMgrRowStatus=_PdnDevTrapMgrRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,9,4,1,6),_PdnDevTrapMgrRowStatus_Type())
pdnDevTrapMgrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDevTrapMgrRowStatus.setStatus(_A)
_PdnDevConfigTrapsEnable_Type=SwitchState
_PdnDevConfigTrapsEnable_Object=MibScalar
pdnDevConfigTrapsEnable=_PdnDevConfigTrapsEnable_Object((1,3,6,1,4,1,1795,2,24,2,9,5),_PdnDevConfigTrapsEnable_Type())
pdnDevConfigTrapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pdnDevConfigTrapsEnable.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'devTrapMgrMaxNumber':devTrapMgrMaxNumber,'devTrapMgrCurrentNumber':devTrapMgrCurrentNumber,'devTrapMgrTable':devTrapMgrTable,'devTrapMgrEntry':devTrapMgrEntry,_G:devTrapMgrIpAddress,'devTrapMgrDestination':devTrapMgrDestination,'devTrapMgrCircuit':devTrapMgrCircuit,'devTrapMgrSubCircuit':devTrapMgrSubCircuit,'pdnDevTrapMgrTable':pdnDevTrapMgrTable,'pdnDevTrapMgrEntry':pdnDevTrapMgrEntry,_H:pdnDevTrapMgrDestAddress,_I:pdnDevTrapMgrSubnetMask,'pdnDevTrapMgrDestPort':pdnDevTrapMgrDestPort,'pdnDevTrapMgrCommunityName':pdnDevTrapMgrCommunityName,'pdnDevTrapMgrEnable':pdnDevTrapMgrEnable,'pdnDevTrapMgrRowStatus':pdnDevTrapMgrRowStatus,'pdnDevConfigTrapsEnable':pdnDevConfigTrapsEnable})