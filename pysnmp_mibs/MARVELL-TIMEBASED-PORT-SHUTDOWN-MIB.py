_I='read-write'
_H='rlTimeBasedPortTimeRangeName'
_G='MARVELL-TIMEBASED-PORT-SHUTDOWN-MIB'
_F='read-only'
_E='DisplayString'
_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlTimeBasedPort=ModuleIdentity((1,3,6,1,4,1,89,208))
if mibBuilder.loadTexts:rlTimeBasedPort.setRevisions(('2011-08-06 00:00',))
_RlTimeBasedPortVersion_Type=Integer32
_RlTimeBasedPortVersion_Object=MibScalar
rlTimeBasedPortVersion=_RlTimeBasedPortVersion_Object((1,3,6,1,4,1,89,208,1),_RlTimeBasedPortVersion_Type())
rlTimeBasedPortVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTimeBasedPortVersion.setStatus(_A)
_RlTimeBasedPortTable_Object=MibTable
rlTimeBasedPortTable=_RlTimeBasedPortTable_Object((1,3,6,1,4,1,89,208,2))
if mibBuilder.loadTexts:rlTimeBasedPortTable.setStatus(_A)
_RlTimeBasedPortEntry_Object=MibTableRow
rlTimeBasedPortEntry=_RlTimeBasedPortEntry_Object((1,3,6,1,4,1,89,208,2,1))
rlTimeBasedPortEntry.setIndexNames((0,_B,_C),(0,_G,_H))
if mibBuilder.loadTexts:rlTimeBasedPortEntry.setStatus(_A)
class _RlTimeBasedPortTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlTimeBasedPortTimeRangeName_Type.__name__=_E
_RlTimeBasedPortTimeRangeName_Object=MibTableColumn
rlTimeBasedPortTimeRangeName=_RlTimeBasedPortTimeRangeName_Object((1,3,6,1,4,1,89,208,2,1,1),_RlTimeBasedPortTimeRangeName_Type())
rlTimeBasedPortTimeRangeName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlTimeBasedPortTimeRangeName.setStatus(_A)
class _RlTimeBasedPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RlTimeBasedPortAction_Type.__name__=_D
_RlTimeBasedPortAction_Object=MibTableColumn
rlTimeBasedPortAction=_RlTimeBasedPortAction_Object((1,3,6,1,4,1,89,208,2,1,2),_RlTimeBasedPortAction_Type())
rlTimeBasedPortAction.setMaxAccess(_I)
if mibBuilder.loadTexts:rlTimeBasedPortAction.setStatus(_A)
_RlTimeBasedPortActive_Type=TruthValue
_RlTimeBasedPortActive_Object=MibTableColumn
rlTimeBasedPortActive=_RlTimeBasedPortActive_Object((1,3,6,1,4,1,89,208,2,1,3),_RlTimeBasedPortActive_Type())
rlTimeBasedPortActive.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTimeBasedPortActive.setStatus(_A)
_RlTimeBasedPortRowStatus_Type=RowStatus
_RlTimeBasedPortRowStatus_Object=MibTableColumn
rlTimeBasedPortRowStatus=_RlTimeBasedPortRowStatus_Object((1,3,6,1,4,1,89,208,2,1,4),_RlTimeBasedPortRowStatus_Type())
rlTimeBasedPortRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:rlTimeBasedPortRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'rlTimeBasedPort':rlTimeBasedPort,'rlTimeBasedPortVersion':rlTimeBasedPortVersion,'rlTimeBasedPortTable':rlTimeBasedPortTable,'rlTimeBasedPortEntry':rlTimeBasedPortEntry,_H:rlTimeBasedPortTimeRangeName,'rlTimeBasedPortAction':rlTimeBasedPortAction,'rlTimeBasedPortActive':rlTimeBasedPortActive,'rlTimeBasedPortRowStatus':rlTimeBasedPortRowStatus})