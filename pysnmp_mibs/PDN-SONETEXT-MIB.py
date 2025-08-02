_L='devSonetStatusLastChange'
_K='read-write'
_J='read-only'
_I='devSonetIfIndex'
_H='sonetSectionCurrentStatus'
_G='sonetPathCurrentStatus'
_F='sonetLineCurrentStatus'
_E='NotificationType'
_D='PDN-SONETEXT-MIB'
_C='Integer32'
_B='SONET-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdnSonetMIB,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnSonetMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonetLineCurrentStatus,sonetPathCurrentStatus,sonetSectionCurrentStatus=mibBuilder.importSymbols(_B,_F,_G,_H)
_DevSonetConfig_ObjectIdentity=ObjectIdentity
devSonetConfig=_DevSonetConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,13,1))
_DevSonetConfigTable_Object=MibTable
devSonetConfigTable=_DevSonetConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1))
if mibBuilder.loadTexts:devSonetConfigTable.setStatus(_A)
_DevSonetConfigEntry_Object=MibTableRow
devSonetConfigEntry=_DevSonetConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1,1))
devSonetConfigEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:devSonetConfigEntry.setStatus(_A)
_DevSonetIfIndex_Type=Integer32
_DevSonetIfIndex_Object=MibTableColumn
devSonetIfIndex=_DevSonetIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1,1,1),_DevSonetIfIndex_Type())
devSonetIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:devSonetIfIndex.setStatus(_A)
class _DevSonetXmitClkSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2),('throughTiming',3),('systemTiming',4)))
_DevSonetXmitClkSrc_Type.__name__=_C
_DevSonetXmitClkSrc_Object=MibTableColumn
devSonetXmitClkSrc=_DevSonetXmitClkSrc_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1,1,2),_DevSonetXmitClkSrc_Type())
devSonetXmitClkSrc.setMaxAccess(_K)
if mibBuilder.loadTexts:devSonetXmitClkSrc.setStatus(_A)
_DevSonetStatusLastChange_Type=TimeTicks
_DevSonetStatusLastChange_Object=MibTableColumn
devSonetStatusLastChange=_DevSonetStatusLastChange_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1,1,3),_DevSonetStatusLastChange_Type())
devSonetStatusLastChange.setMaxAccess(_J)
if mibBuilder.loadTexts:devSonetStatusLastChange.setStatus(_A)
class _DevSonetStatusChangeTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_DevSonetStatusChangeTrapEnable_Type.__name__=_C
_DevSonetStatusChangeTrapEnable_Object=MibTableColumn
devSonetStatusChangeTrapEnable=_DevSonetStatusChangeTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,6,13,1,1,1,4),_DevSonetStatusChangeTrapEnable_Type())
devSonetStatusChangeTrapEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:devSonetStatusChangeTrapEnable.setStatus(_A)
_DevSonetTraps_ObjectIdentity=ObjectIdentity
devSonetTraps=_DevSonetTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,13,2))
devSonetStatusChange=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,13,2,0,1))
devSonetStatusChange.setObjects(*((_D,_L),(_B,_H),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:devSonetStatusChange.setStatus('')
mibBuilder.exportSymbols(_D,**{'devSonetConfig':devSonetConfig,'devSonetConfigTable':devSonetConfigTable,'devSonetConfigEntry':devSonetConfigEntry,_I:devSonetIfIndex,'devSonetXmitClkSrc':devSonetXmitClkSrc,_L:devSonetStatusLastChange,'devSonetStatusChangeTrapEnable':devSonetStatusChangeTrapEnable,'devSonetTraps':devSonetTraps,'devSonetStatusChange':devSonetStatusChange})