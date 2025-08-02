_H='snIgmpStaticGroupAddress'
_G='snIgmpStaticGroupIfIndex'
_F='snIgmpIfEntryIndex'
_E='FOUNDRY-SN-IGMP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
router,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','router')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snIgmp=ModuleIdentity((1,3,6,1,4,1,1991,1,2,6))
if mibBuilder.loadTexts:snIgmp.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
_SnIgmpMIBObjects_ObjectIdentity=ObjectIdentity
snIgmpMIBObjects=_SnIgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,2,6,1))
class _SnIgmpQueryInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_SnIgmpQueryInterval_Type.__name__=_C
_SnIgmpQueryInterval_Object=MibScalar
snIgmpQueryInterval=_SnIgmpQueryInterval_Object((1,3,6,1,4,1,1991,1,2,6,1,1),_SnIgmpQueryInterval_Type())
snIgmpQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:snIgmpQueryInterval.setStatus(_A)
class _SnIgmpGroupMembershipTime_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_SnIgmpGroupMembershipTime_Type.__name__=_C
_SnIgmpGroupMembershipTime_Object=MibScalar
snIgmpGroupMembershipTime=_SnIgmpGroupMembershipTime_Object((1,3,6,1,4,1,1991,1,2,6,1,2),_SnIgmpGroupMembershipTime_Type())
snIgmpGroupMembershipTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snIgmpGroupMembershipTime.setStatus(_A)
_SnIgmpIfTable_Object=MibTable
snIgmpIfTable=_SnIgmpIfTable_Object((1,3,6,1,4,1,1991,1,2,6,1,3))
if mibBuilder.loadTexts:snIgmpIfTable.setStatus(_A)
_SnIgmpIfEntry_Object=MibTableRow
snIgmpIfEntry=_SnIgmpIfEntry_Object((1,3,6,1,4,1,1991,1,2,6,1,3,1))
snIgmpIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:snIgmpIfEntry.setStatus(_A)
_SnIgmpIfEntryIndex_Type=Integer32
_SnIgmpIfEntryIndex_Object=MibTableColumn
snIgmpIfEntryIndex=_SnIgmpIfEntryIndex_Object((1,3,6,1,4,1,1991,1,2,6,1,3,1,1),_SnIgmpIfEntryIndex_Type())
snIgmpIfEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpIfEntryIndex.setStatus(_A)
_SnIgmpIfPortNumber_Type=Integer32
_SnIgmpIfPortNumber_Object=MibTableColumn
snIgmpIfPortNumber=_SnIgmpIfPortNumber_Object((1,3,6,1,4,1,1991,1,2,6,1,3,1,2),_SnIgmpIfPortNumber_Type())
snIgmpIfPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpIfPortNumber.setStatus(_A)
_SnIgmpIfGroupAddress_Type=IpAddress
_SnIgmpIfGroupAddress_Object=MibTableColumn
snIgmpIfGroupAddress=_SnIgmpIfGroupAddress_Object((1,3,6,1,4,1,1991,1,2,6,1,3,1,3),_SnIgmpIfGroupAddress_Type())
snIgmpIfGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpIfGroupAddress.setStatus(_A)
_SnIgmpIfGroupAge_Type=Integer32
_SnIgmpIfGroupAge_Object=MibTableColumn
snIgmpIfGroupAge=_SnIgmpIfGroupAge_Object((1,3,6,1,4,1,1991,1,2,6,1,3,1,4),_SnIgmpIfGroupAge_Type())
snIgmpIfGroupAge.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpIfGroupAge.setStatus(_A)
_SnIgmpStaticGroupTable_Object=MibTable
snIgmpStaticGroupTable=_SnIgmpStaticGroupTable_Object((1,3,6,1,4,1,1991,1,2,6,1,4))
if mibBuilder.loadTexts:snIgmpStaticGroupTable.setStatus(_A)
_SnIgmpStaticGroupEntry_Object=MibTableRow
snIgmpStaticGroupEntry=_SnIgmpStaticGroupEntry_Object((1,3,6,1,4,1,1991,1,2,6,1,4,1))
snIgmpStaticGroupEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:snIgmpStaticGroupEntry.setStatus(_A)
_SnIgmpStaticGroupIfIndex_Type=Integer32
_SnIgmpStaticGroupIfIndex_Object=MibTableColumn
snIgmpStaticGroupIfIndex=_SnIgmpStaticGroupIfIndex_Object((1,3,6,1,4,1,1991,1,2,6,1,4,1,1),_SnIgmpStaticGroupIfIndex_Type())
snIgmpStaticGroupIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpStaticGroupIfIndex.setStatus(_A)
_SnIgmpStaticGroupAddress_Type=IpAddress
_SnIgmpStaticGroupAddress_Object=MibTableColumn
snIgmpStaticGroupAddress=_SnIgmpStaticGroupAddress_Object((1,3,6,1,4,1,1991,1,2,6,1,4,1,2),_SnIgmpStaticGroupAddress_Type())
snIgmpStaticGroupAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snIgmpStaticGroupAddress.setStatus(_A)
_SnIgmpStaticGroupPortList_Type=OctetString
_SnIgmpStaticGroupPortList_Object=MibTableColumn
snIgmpStaticGroupPortList=_SnIgmpStaticGroupPortList_Object((1,3,6,1,4,1,1991,1,2,6,1,4,1,3),_SnIgmpStaticGroupPortList_Type())
snIgmpStaticGroupPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snIgmpStaticGroupPortList.setStatus(_A)
class _SnIgmpStaticGroupRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('valid',2),('delete',3),('create',4),('modify',5)))
_SnIgmpStaticGroupRowStatus_Type.__name__=_C
_SnIgmpStaticGroupRowStatus_Object=MibTableColumn
snIgmpStaticGroupRowStatus=_SnIgmpStaticGroupRowStatus_Object((1,3,6,1,4,1,1991,1,2,6,1,4,1,4),_SnIgmpStaticGroupRowStatus_Type())
snIgmpStaticGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snIgmpStaticGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'snIgmp':snIgmp,'snIgmpMIBObjects':snIgmpMIBObjects,'snIgmpQueryInterval':snIgmpQueryInterval,'snIgmpGroupMembershipTime':snIgmpGroupMembershipTime,'snIgmpIfTable':snIgmpIfTable,'snIgmpIfEntry':snIgmpIfEntry,_F:snIgmpIfEntryIndex,'snIgmpIfPortNumber':snIgmpIfPortNumber,'snIgmpIfGroupAddress':snIgmpIfGroupAddress,'snIgmpIfGroupAge':snIgmpIfGroupAge,'snIgmpStaticGroupTable':snIgmpStaticGroupTable,'snIgmpStaticGroupEntry':snIgmpStaticGroupEntry,_G:snIgmpStaticGroupIfIndex,_H:snIgmpStaticGroupAddress,'snIgmpStaticGroupPortList':snIgmpStaticGroupPortList,'snIgmpStaticGroupRowStatus':snIgmpStaticGroupRowStatus})