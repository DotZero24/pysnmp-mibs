_K='eltexULDLinkStatus'
_J='ELTEX-ULD-MIB'
_I='read-only'
_H='disabled'
_G='enabled'
_F='TruthValue'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
eltexULDMIB=ModuleIdentity((1,3,6,1,4,1,35265,34))
_EltexULDNotifications_ObjectIdentity=ObjectIdentity
eltexULDNotifications=_EltexULDNotifications_ObjectIdentity((1,3,6,1,4,1,35265,34,0))
_EltexULDMgmt_ObjectIdentity=ObjectIdentity
eltexULDMgmt=_EltexULDMgmt_ObjectIdentity((1,3,6,1,4,1,35265,34,1))
_EltexULDTable_Object=MibTable
eltexULDTable=_EltexULDTable_Object((1,3,6,1,4,1,35265,34,1,1))
if mibBuilder.loadTexts:eltexULDTable.setStatus(_A)
_EltexULDEntry_Object=MibTableRow
eltexULDEntry=_EltexULDEntry_Object((1,3,6,1,4,1,35265,34,1,1,1))
eltexULDEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltexULDEntry.setStatus(_A)
class _EltexULDAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EltexULDAdminState_Type.__name__=_B
_EltexULDAdminState_Object=MibTableColumn
eltexULDAdminState=_EltexULDAdminState_Object((1,3,6,1,4,1,35265,34,1,1,1,1),_EltexULDAdminState_Type())
eltexULDAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexULDAdminState.setStatus(_A)
class _EltexULDOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EltexULDOperStatus_Type.__name__=_B
_EltexULDOperStatus_Object=MibTableColumn
eltexULDOperStatus=_EltexULDOperStatus_Object((1,3,6,1,4,1,35265,34,1,1,1,2),_EltexULDOperStatus_Type())
eltexULDOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexULDOperStatus.setStatus(_A)
class _EltexULDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('log',1),('err-disable',2)))
_EltexULDMode_Type.__name__=_B
_EltexULDMode_Object=MibTableColumn
eltexULDMode=_EltexULDMode_Object((1,3,6,1,4,1,35265,34,1,1,1,3),_EltexULDMode_Type())
eltexULDMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexULDMode.setStatus(_A)
class _EltexULDDiscoveryTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_EltexULDDiscoveryTime_Type.__name__=_B
_EltexULDDiscoveryTime_Object=MibTableColumn
eltexULDDiscoveryTime=_EltexULDDiscoveryTime_Object((1,3,6,1,4,1,35265,34,1,1,1,4),_EltexULDDiscoveryTime_Type())
eltexULDDiscoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexULDDiscoveryTime.setStatus(_A)
class _EltexULDIsAggressive_Type(TruthValue):defaultValue=2
_EltexULDIsAggressive_Type.__name__=_F
_EltexULDIsAggressive_Object=MibTableColumn
eltexULDIsAggressive=_EltexULDIsAggressive_Object((1,3,6,1,4,1,35265,34,1,1,1,5),_EltexULDIsAggressive_Type())
eltexULDIsAggressive.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexULDIsAggressive.setStatus(_A)
class _EltexULDLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('unidirectional',2),('bidirectional',3),('tx-rx-loop',4),('neighbor-mismatch',5)))
_EltexULDLinkStatus_Type.__name__=_B
_EltexULDLinkStatus_Object=MibTableColumn
eltexULDLinkStatus=_EltexULDLinkStatus_Object((1,3,6,1,4,1,35265,34,1,1,1,6),_EltexULDLinkStatus_Type())
eltexULDLinkStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltexULDLinkStatus.setStatus(_A)
eltexULDLinkStatusChanged=NotificationType((1,3,6,1,4,1,35265,34,0,1))
eltexULDLinkStatusChanged.setObjects(*((_D,_E),(_J,_K)))
if mibBuilder.loadTexts:eltexULDLinkStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'eltexULDMIB':eltexULDMIB,'eltexULDNotifications':eltexULDNotifications,'eltexULDLinkStatusChanged':eltexULDLinkStatusChanged,'eltexULDMgmt':eltexULDMgmt,'eltexULDTable':eltexULDTable,'eltexULDEntry':eltexULDEntry,'eltexULDAdminState':eltexULDAdminState,'eltexULDOperStatus':eltexULDOperStatus,'eltexULDMode':eltexULDMode,'eltexULDDiscoveryTime':eltexULDDiscoveryTime,'eltexULDIsAggressive':eltexULDIsAggressive,_K:eltexULDLinkStatus})