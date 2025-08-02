_H='read-only'
_G='disabled'
_F='enabled'
_E='swDULDPort'
_D='DULD-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swDULDMIB=ModuleIdentity((1,3,6,1,4,1,171,12,87))
_SwDULDMgmt_ObjectIdentity=ObjectIdentity
swDULDMgmt=_SwDULDMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,87,1))
_SwDULDTable_Object=MibTable
swDULDTable=_SwDULDTable_Object((1,3,6,1,4,1,171,12,87,1,1))
if mibBuilder.loadTexts:swDULDTable.setStatus(_A)
_SwDULDEntry_Object=MibTableRow
swDULDEntry=_SwDULDEntry_Object((1,3,6,1,4,1,171,12,87,1,1,1))
swDULDEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swDULDEntry.setStatus(_A)
_SwDULDPort_Type=Integer32
_SwDULDPort_Object=MibTableColumn
swDULDPort=_SwDULDPort_Object((1,3,6,1,4,1,171,12,87,1,1,1,1),_SwDULDPort_Type())
swDULDPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swDULDPort.setStatus(_A)
class _SwDULDAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwDULDAdminState_Type.__name__=_B
_SwDULDAdminState_Object=MibTableColumn
swDULDAdminState=_SwDULDAdminState_Object((1,3,6,1,4,1,171,12,87,1,1,1,2),_SwDULDAdminState_Type())
swDULDAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swDULDAdminState.setStatus(_A)
class _SwDULDOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwDULDOperStatus_Type.__name__=_B
_SwDULDOperStatus_Object=MibTableColumn
swDULDOperStatus=_SwDULDOperStatus_Object((1,3,6,1,4,1,171,12,87,1,1,1,3),_SwDULDOperStatus_Type())
swDULDOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swDULDOperStatus.setStatus(_A)
class _SwDULDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shutdown',1),('normal',2)))
_SwDULDMode_Type.__name__=_B
_SwDULDMode_Object=MibTableColumn
swDULDMode=_SwDULDMode_Object((1,3,6,1,4,1,171,12,87,1,1,1,4),_SwDULDMode_Type())
swDULDMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swDULDMode.setStatus(_A)
class _SwDULDDiscoveryTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65535))
_SwDULDDiscoveryTime_Type.__name__=_B
_SwDULDDiscoveryTime_Object=MibTableColumn
swDULDDiscoveryTime=_SwDULDDiscoveryTime_Object((1,3,6,1,4,1,171,12,87,1,1,1,5),_SwDULDDiscoveryTime_Type())
swDULDDiscoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swDULDDiscoveryTime.setStatus(_A)
if mibBuilder.loadTexts:swDULDDiscoveryTime.setUnits('seconds')
class _SwDULDLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('bidirectional',2),('tx-fault',3),('rx-fault',4),('link-down',5)))
_SwDULDLinkStatus_Type.__name__=_B
_SwDULDLinkStatus_Object=MibTableColumn
swDULDLinkStatus=_SwDULDLinkStatus_Object((1,3,6,1,4,1,171,12,87,1,1,1,6),_SwDULDLinkStatus_Type())
swDULDLinkStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swDULDLinkStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swDULDMIB':swDULDMIB,'swDULDMgmt':swDULDMgmt,'swDULDTable':swDULDTable,'swDULDEntry':swDULDEntry,_E:swDULDPort,'swDULDAdminState':swDULDAdminState,'swDULDOperStatus':swDULDOperStatus,'swDULDMode':swDULDMode,'swDULDDiscoveryTime':swDULDDiscoveryTime,'swDULDLinkStatus':swDULDLinkStatus})