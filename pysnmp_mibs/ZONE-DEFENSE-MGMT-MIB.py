_H='swZoneDefenseMacAddress'
_G='not-accessible'
_F='swZoneDefenseAddress'
_E='read-only'
_D='ZONE-DEFENSE-MGMT-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swZoneDefenseMIB=ModuleIdentity((1,3,6,1,4,1,171,12,92))
_SwZoneDefenseMIBObjects_ObjectIdentity=ObjectIdentity
swZoneDefenseMIBObjects=_SwZoneDefenseMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,92,1))
_SwZoneDefenseTable_Object=MibTable
swZoneDefenseTable=_SwZoneDefenseTable_Object((1,3,6,1,4,1,171,12,92,1,1))
if mibBuilder.loadTexts:swZoneDefenseTable.setStatus(_A)
_SwZoneDefenseEntry_Object=MibTableRow
swZoneDefenseEntry=_SwZoneDefenseEntry_Object((1,3,6,1,4,1,171,12,92,1,1,1))
swZoneDefenseEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:swZoneDefenseEntry.setStatus(_A)
_SwZoneDefenseAddress_Type=IpAddress
_SwZoneDefenseAddress_Object=MibTableColumn
swZoneDefenseAddress=_SwZoneDefenseAddress_Object((1,3,6,1,4,1,171,12,92,1,1,1,1),_SwZoneDefenseAddress_Type())
swZoneDefenseAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:swZoneDefenseAddress.setStatus(_A)
_SwZoneDefenseRowStatus_Type=RowStatus
_SwZoneDefenseRowStatus_Object=MibTableColumn
swZoneDefenseRowStatus=_SwZoneDefenseRowStatus_Object((1,3,6,1,4,1,171,12,92,1,1,1,2),_SwZoneDefenseRowStatus_Type())
swZoneDefenseRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseRowStatus.setStatus(_A)
class _SwZoneDefenseProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('icmp',2),('tcp',3),('udp',4)))
_SwZoneDefenseProtocol_Type.__name__=_B
_SwZoneDefenseProtocol_Object=MibTableColumn
swZoneDefenseProtocol=_SwZoneDefenseProtocol_Object((1,3,6,1,4,1,171,12,92,1,1,1,3),_SwZoneDefenseProtocol_Type())
swZoneDefenseProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseProtocol.setStatus(_A)
class _SwZoneDefenseDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_SwZoneDefenseDstPort_Type.__name__=_B
_SwZoneDefenseDstPort_Object=MibTableColumn
swZoneDefenseDstPort=_SwZoneDefenseDstPort_Object((1,3,6,1,4,1,171,12,92,1,1,1,4),_SwZoneDefenseDstPort_Type())
swZoneDefenseDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseDstPort.setStatus(_A)
_SwZoneDefenseMacTable_Object=MibTable
swZoneDefenseMacTable=_SwZoneDefenseMacTable_Object((1,3,6,1,4,1,171,12,92,1,2))
if mibBuilder.loadTexts:swZoneDefenseMacTable.setStatus(_A)
_SwZoneDefenseMacEntry_Object=MibTableRow
swZoneDefenseMacEntry=_SwZoneDefenseMacEntry_Object((1,3,6,1,4,1,171,12,92,1,2,1))
swZoneDefenseMacEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:swZoneDefenseMacEntry.setStatus(_A)
_SwZoneDefenseMacAddress_Type=MacAddress
_SwZoneDefenseMacAddress_Object=MibTableColumn
swZoneDefenseMacAddress=_SwZoneDefenseMacAddress_Object((1,3,6,1,4,1,171,12,92,1,2,1,1),_SwZoneDefenseMacAddress_Type())
swZoneDefenseMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:swZoneDefenseMacAddress.setStatus(_A)
_SwZoneDefenseMacRowStatus_Type=RowStatus
_SwZoneDefenseMacRowStatus_Object=MibTableColumn
swZoneDefenseMacRowStatus=_SwZoneDefenseMacRowStatus_Object((1,3,6,1,4,1,171,12,92,1,2,1,2),_SwZoneDefenseMacRowStatus_Type())
swZoneDefenseMacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseMacRowStatus.setStatus(_A)
class _SwZoneDefenseMacProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all',1),('icmp',2),('tcp',3),('udp',4)))
_SwZoneDefenseMacProtocol_Type.__name__=_B
_SwZoneDefenseMacProtocol_Object=MibTableColumn
swZoneDefenseMacProtocol=_SwZoneDefenseMacProtocol_Object((1,3,6,1,4,1,171,12,92,1,2,1,3),_SwZoneDefenseMacProtocol_Type())
swZoneDefenseMacProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseMacProtocol.setStatus(_A)
class _SwZoneDefenseMacDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_SwZoneDefenseMacDstPort_Type.__name__=_B
_SwZoneDefenseMacDstPort_Object=MibTableColumn
swZoneDefenseMacDstPort=_SwZoneDefenseMacDstPort_Object((1,3,6,1,4,1,171,12,92,1,2,1,4),_SwZoneDefenseMacDstPort_Type())
swZoneDefenseMacDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swZoneDefenseMacDstPort.setStatus(_A)
class _SwZoneDefenseStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwZoneDefenseStatus_Type.__name__=_B
_SwZoneDefenseStatus_Object=MibScalar
swZoneDefenseStatus=_SwZoneDefenseStatus_Object((1,3,6,1,4,1,171,12,92,1,3),_SwZoneDefenseStatus_Type())
swZoneDefenseStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:swZoneDefenseStatus.setStatus(_A)
_SwZoneDefenseRemains_Type=Integer32
_SwZoneDefenseRemains_Object=MibScalar
swZoneDefenseRemains=_SwZoneDefenseRemains_Object((1,3,6,1,4,1,171,12,92,1,4),_SwZoneDefenseRemains_Type())
swZoneDefenseRemains.setMaxAccess(_E)
if mibBuilder.loadTexts:swZoneDefenseRemains.setStatus(_A)
_SwZoneDefenseIpRemains_Type=Integer32
_SwZoneDefenseIpRemains_Object=MibScalar
swZoneDefenseIpRemains=_SwZoneDefenseIpRemains_Object((1,3,6,1,4,1,171,12,92,1,5),_SwZoneDefenseIpRemains_Type())
swZoneDefenseIpRemains.setMaxAccess(_E)
if mibBuilder.loadTexts:swZoneDefenseIpRemains.setStatus(_A)
_SwZoneDefenseMacRemains_Type=Integer32
_SwZoneDefenseMacRemains_Object=MibScalar
swZoneDefenseMacRemains=_SwZoneDefenseMacRemains_Object((1,3,6,1,4,1,171,12,92,1,6),_SwZoneDefenseMacRemains_Type())
swZoneDefenseMacRemains.setMaxAccess(_E)
if mibBuilder.loadTexts:swZoneDefenseMacRemains.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swZoneDefenseMIB':swZoneDefenseMIB,'swZoneDefenseMIBObjects':swZoneDefenseMIBObjects,'swZoneDefenseTable':swZoneDefenseTable,'swZoneDefenseEntry':swZoneDefenseEntry,_F:swZoneDefenseAddress,'swZoneDefenseRowStatus':swZoneDefenseRowStatus,'swZoneDefenseProtocol':swZoneDefenseProtocol,'swZoneDefenseDstPort':swZoneDefenseDstPort,'swZoneDefenseMacTable':swZoneDefenseMacTable,'swZoneDefenseMacEntry':swZoneDefenseMacEntry,_H:swZoneDefenseMacAddress,'swZoneDefenseMacRowStatus':swZoneDefenseMacRowStatus,'swZoneDefenseMacProtocol':swZoneDefenseMacProtocol,'swZoneDefenseMacDstPort':swZoneDefenseMacDstPort,'swZoneDefenseStatus':swZoneDefenseStatus,'swZoneDefenseRemains':swZoneDefenseRemains,'swZoneDefenseIpRemains':swZoneDefenseIpRemains,'swZoneDefenseMacRemains':swZoneDefenseMacRemains})