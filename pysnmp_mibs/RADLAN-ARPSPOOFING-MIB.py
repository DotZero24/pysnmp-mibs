_F='rlArpSpoofingLocalIpAddr'
_E='rlArpSpoofingIfIndex'
_D='InterfaceIndexOrZero'
_C='RADLAN-ARPSPOOFING-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_D)
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rlArpSpoofing=ModuleIdentity((1,3,6,1,4,1,89,60))
if mibBuilder.loadTexts:rlArpSpoofing.setRevisions(('2007-01-02 00:00',))
_RlArpSpoofingMibVersion_Type=Integer32
_RlArpSpoofingMibVersion_Object=MibScalar
rlArpSpoofingMibVersion=_RlArpSpoofingMibVersion_Object((1,3,6,1,4,1,89,60,1),_RlArpSpoofingMibVersion_Type())
rlArpSpoofingMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlArpSpoofingMibVersion.setStatus(_A)
_RlArpSpoofingTable_Object=MibTable
rlArpSpoofingTable=_RlArpSpoofingTable_Object((1,3,6,1,4,1,89,60,2))
if mibBuilder.loadTexts:rlArpSpoofingTable.setStatus(_A)
_RlArpSpoofingEntry_Object=MibTableRow
rlArpSpoofingEntry=_RlArpSpoofingEntry_Object((1,3,6,1,4,1,89,60,2,1))
rlArpSpoofingEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:rlArpSpoofingEntry.setStatus(_A)
_RlArpSpoofingIfIndex_Type=InterfaceIndex
_RlArpSpoofingIfIndex_Object=MibTableColumn
rlArpSpoofingIfIndex=_RlArpSpoofingIfIndex_Object((1,3,6,1,4,1,89,60,2,1,1),_RlArpSpoofingIfIndex_Type())
rlArpSpoofingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingIfIndex.setStatus(_A)
_RlArpSpoofingLocalIpAddr_Type=IpAddress
_RlArpSpoofingLocalIpAddr_Object=MibTableColumn
rlArpSpoofingLocalIpAddr=_RlArpSpoofingLocalIpAddr_Object((1,3,6,1,4,1,89,60,2,1,2),_RlArpSpoofingLocalIpAddr_Type())
rlArpSpoofingLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingLocalIpAddr.setStatus(_A)
_RlArpSpoofingMacAddr_Type=PhysAddress
_RlArpSpoofingMacAddr_Object=MibTableColumn
rlArpSpoofingMacAddr=_RlArpSpoofingMacAddr_Object((1,3,6,1,4,1,89,60,2,1,3),_RlArpSpoofingMacAddr_Type())
rlArpSpoofingMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingMacAddr.setStatus(_A)
_RlArpSpoofingRemoteIpAddr_Type=IpAddress
_RlArpSpoofingRemoteIpAddr_Object=MibTableColumn
rlArpSpoofingRemoteIpAddr=_RlArpSpoofingRemoteIpAddr_Object((1,3,6,1,4,1,89,60,2,1,4),_RlArpSpoofingRemoteIpAddr_Type())
rlArpSpoofingRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingRemoteIpAddr.setStatus(_A)
class _RlArpSpoofingOutPhysIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_RlArpSpoofingOutPhysIfIndex_Type.__name__=_D
_RlArpSpoofingOutPhysIfIndex_Object=MibTableColumn
rlArpSpoofingOutPhysIfIndex=_RlArpSpoofingOutPhysIfIndex_Object((1,3,6,1,4,1,89,60,2,1,5),_RlArpSpoofingOutPhysIfIndex_Type())
rlArpSpoofingOutPhysIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingOutPhysIfIndex.setStatus(_A)
_RlArpSpoofingStatus_Type=RowStatus
_RlArpSpoofingStatus_Object=MibTableColumn
rlArpSpoofingStatus=_RlArpSpoofingStatus_Object((1,3,6,1,4,1,89,60,2,1,6),_RlArpSpoofingStatus_Type())
rlArpSpoofingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlArpSpoofingStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rlArpSpoofing':rlArpSpoofing,'rlArpSpoofingMibVersion':rlArpSpoofingMibVersion,'rlArpSpoofingTable':rlArpSpoofingTable,'rlArpSpoofingEntry':rlArpSpoofingEntry,_E:rlArpSpoofingIfIndex,_F:rlArpSpoofingLocalIpAddr,'rlArpSpoofingMacAddr':rlArpSpoofingMacAddr,'rlArpSpoofingRemoteIpAddr':rlArpSpoofingRemoteIpAddr,'rlArpSpoofingOutPhysIfIndex':rlArpSpoofingOutPhysIfIndex,'rlArpSpoofingStatus':rlArpSpoofingStatus})