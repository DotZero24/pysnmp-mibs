_e='altigaAddressStatsGroupSup1'
_d='alAddressStatsGrpHeldReason'
_c='alAddressStatsGrpHeldTimeLeft'
_b='alAddressStatsGrpHeldAddress'
_a='alAddressStatsHeldReason'
_Z='alAddressStatsHeldTimeLeft'
_Y='alAddressStatsHeldAddress'
_X='alAddressStatsGrpHeldAddresses'
_W='alAddressStatsHeldAddresses'
_V='alAddressStatsGrpMaxAddressesAssigned'
_U='alAddressStatsGrpCurrAvailAddresses'
_T='alAddressStatsGrpCurrAllocAddresses'
_S='alAddressStatsGrpTotalPoolAddresses'
_R='alAddressStatsMaxAddressesAssigned'
_Q='alAddressStatsCurrAvailAddresses'
_P='alAddressStatsCurrAllocAddresses'
_O='alAddressStatsTotalPoolAddresses'
_N='seconds'
_M='altigaAddressStatsGroup'
_L='alAddressStatsGrpHeldAddrIndex'
_K='alAddressStatsGrpHeldPoolId'
_J='alAddressStatsGrpHeldId'
_I='alAddressStatsHeldAddrIndex'
_H='alAddressStatsHeldPoolId'
_G='alAddressStatsGrpPoolId'
_F='alAddressStatsGrpId'
_E='alAddressStatsPoolId'
_D='Integer32'
_C='read-only'
_B='ALTIGA-ADDRESS-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alAddressMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alAddressMibModule')
alAddressGroup,alStatsAddress=mibBuilder.importSymbols('ALTIGA-MIB','alAddressGroup','alStatsAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaAddressStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,24,2))
if mibBuilder.loadTexts:altigaAddressStatsMibModule.setRevisions(('2005-01-25 00:00','2002-09-05 13:00','2002-07-10 00:00'))
class IPAddressHeldReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delayReuse',1),('foundInUse',2)))
_AltigaAddressStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaAddressStatsMibConformance=_AltigaAddressStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,24,2,1))
_AltigaAddressStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaAddressStatsMibCompliances=_AltigaAddressStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,24,2,1,1))
_AlAddressStatsGlobal_ObjectIdentity=ObjectIdentity
alAddressStatsGlobal=_AlAddressStatsGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,19,1))
_AlAddressStatsPoolTable_Object=MibTable
alAddressStatsPoolTable=_AlAddressStatsPoolTable_Object((1,3,6,1,4,1,3076,2,1,2,19,2))
if mibBuilder.loadTexts:alAddressStatsPoolTable.setStatus(_A)
_AlAddressStatsPoolEntry_Object=MibTableRow
alAddressStatsPoolEntry=_AlAddressStatsPoolEntry_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1))
alAddressStatsPoolEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:alAddressStatsPoolEntry.setStatus(_A)
class _AlAddressStatsPoolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsPoolId_Type.__name__=_D
_AlAddressStatsPoolId_Object=MibTableColumn
alAddressStatsPoolId=_AlAddressStatsPoolId_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,1),_AlAddressStatsPoolId_Type())
alAddressStatsPoolId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsPoolId.setStatus(_A)
class _AlAddressStatsTotalPoolAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsTotalPoolAddresses_Type.__name__=_D
_AlAddressStatsTotalPoolAddresses_Object=MibTableColumn
alAddressStatsTotalPoolAddresses=_AlAddressStatsTotalPoolAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,2),_AlAddressStatsTotalPoolAddresses_Type())
alAddressStatsTotalPoolAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsTotalPoolAddresses.setStatus(_A)
_AlAddressStatsCurrAllocAddresses_Type=Gauge32
_AlAddressStatsCurrAllocAddresses_Object=MibTableColumn
alAddressStatsCurrAllocAddresses=_AlAddressStatsCurrAllocAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,3),_AlAddressStatsCurrAllocAddresses_Type())
alAddressStatsCurrAllocAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsCurrAllocAddresses.setStatus(_A)
_AlAddressStatsCurrAvailAddresses_Type=Gauge32
_AlAddressStatsCurrAvailAddresses_Object=MibTableColumn
alAddressStatsCurrAvailAddresses=_AlAddressStatsCurrAvailAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,4),_AlAddressStatsCurrAvailAddresses_Type())
alAddressStatsCurrAvailAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsCurrAvailAddresses.setStatus(_A)
_AlAddressStatsMaxAddressesAssigned_Type=Gauge32
_AlAddressStatsMaxAddressesAssigned_Object=MibTableColumn
alAddressStatsMaxAddressesAssigned=_AlAddressStatsMaxAddressesAssigned_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,5),_AlAddressStatsMaxAddressesAssigned_Type())
alAddressStatsMaxAddressesAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsMaxAddressesAssigned.setStatus(_A)
_AlAddressStatsHeldAddresses_Type=Gauge32
_AlAddressStatsHeldAddresses_Object=MibTableColumn
alAddressStatsHeldAddresses=_AlAddressStatsHeldAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,2,1,6),_AlAddressStatsHeldAddresses_Type())
alAddressStatsHeldAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldAddresses.setStatus(_A)
_AlAddressStatsPoolGroupTable_Object=MibTable
alAddressStatsPoolGroupTable=_AlAddressStatsPoolGroupTable_Object((1,3,6,1,4,1,3076,2,1,2,19,3))
if mibBuilder.loadTexts:alAddressStatsPoolGroupTable.setStatus(_A)
_AlAddressStatsPoolGroupEntry_Object=MibTableRow
alAddressStatsPoolGroupEntry=_AlAddressStatsPoolGroupEntry_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1))
alAddressStatsPoolGroupEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:alAddressStatsPoolGroupEntry.setStatus(_A)
class _AlAddressStatsGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpId_Type.__name__=_D
_AlAddressStatsGrpId_Object=MibTableColumn
alAddressStatsGrpId=_AlAddressStatsGrpId_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,1),_AlAddressStatsGrpId_Type())
alAddressStatsGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpId.setStatus(_A)
class _AlAddressStatsGrpPoolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpPoolId_Type.__name__=_D
_AlAddressStatsGrpPoolId_Object=MibTableColumn
alAddressStatsGrpPoolId=_AlAddressStatsGrpPoolId_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,2),_AlAddressStatsGrpPoolId_Type())
alAddressStatsGrpPoolId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpPoolId.setStatus(_A)
class _AlAddressStatsGrpTotalPoolAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpTotalPoolAddresses_Type.__name__=_D
_AlAddressStatsGrpTotalPoolAddresses_Object=MibTableColumn
alAddressStatsGrpTotalPoolAddresses=_AlAddressStatsGrpTotalPoolAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,3),_AlAddressStatsGrpTotalPoolAddresses_Type())
alAddressStatsGrpTotalPoolAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpTotalPoolAddresses.setStatus(_A)
_AlAddressStatsGrpCurrAllocAddresses_Type=Gauge32
_AlAddressStatsGrpCurrAllocAddresses_Object=MibTableColumn
alAddressStatsGrpCurrAllocAddresses=_AlAddressStatsGrpCurrAllocAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,4),_AlAddressStatsGrpCurrAllocAddresses_Type())
alAddressStatsGrpCurrAllocAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpCurrAllocAddresses.setStatus(_A)
_AlAddressStatsGrpCurrAvailAddresses_Type=Gauge32
_AlAddressStatsGrpCurrAvailAddresses_Object=MibTableColumn
alAddressStatsGrpCurrAvailAddresses=_AlAddressStatsGrpCurrAvailAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,5),_AlAddressStatsGrpCurrAvailAddresses_Type())
alAddressStatsGrpCurrAvailAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpCurrAvailAddresses.setStatus(_A)
_AlAddressStatsGrpMaxAddressesAssigned_Type=Gauge32
_AlAddressStatsGrpMaxAddressesAssigned_Object=MibTableColumn
alAddressStatsGrpMaxAddressesAssigned=_AlAddressStatsGrpMaxAddressesAssigned_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,6),_AlAddressStatsGrpMaxAddressesAssigned_Type())
alAddressStatsGrpMaxAddressesAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpMaxAddressesAssigned.setStatus(_A)
_AlAddressStatsGrpHeldAddresses_Type=Gauge32
_AlAddressStatsGrpHeldAddresses_Object=MibTableColumn
alAddressStatsGrpHeldAddresses=_AlAddressStatsGrpHeldAddresses_Object((1,3,6,1,4,1,3076,2,1,2,19,3,1,7),_AlAddressStatsGrpHeldAddresses_Type())
alAddressStatsGrpHeldAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldAddresses.setStatus(_A)
_AlAddressStatsHeldTable_Object=MibTable
alAddressStatsHeldTable=_AlAddressStatsHeldTable_Object((1,3,6,1,4,1,3076,2,1,2,19,4))
if mibBuilder.loadTexts:alAddressStatsHeldTable.setStatus(_A)
_AlAddressStatsHeldEntry_Object=MibTableRow
alAddressStatsHeldEntry=_AlAddressStatsHeldEntry_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1))
alAddressStatsHeldEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:alAddressStatsHeldEntry.setStatus(_A)
class _AlAddressStatsHeldPoolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsHeldPoolId_Type.__name__=_D
_AlAddressStatsHeldPoolId_Object=MibTableColumn
alAddressStatsHeldPoolId=_AlAddressStatsHeldPoolId_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1,1),_AlAddressStatsHeldPoolId_Type())
alAddressStatsHeldPoolId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldPoolId.setStatus(_A)
class _AlAddressStatsHeldAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsHeldAddrIndex_Type.__name__=_D
_AlAddressStatsHeldAddrIndex_Object=MibTableColumn
alAddressStatsHeldAddrIndex=_AlAddressStatsHeldAddrIndex_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1,2),_AlAddressStatsHeldAddrIndex_Type())
alAddressStatsHeldAddrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldAddrIndex.setStatus(_A)
_AlAddressStatsHeldAddress_Type=IpAddress
_AlAddressStatsHeldAddress_Object=MibTableColumn
alAddressStatsHeldAddress=_AlAddressStatsHeldAddress_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1,3),_AlAddressStatsHeldAddress_Type())
alAddressStatsHeldAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldAddress.setStatus(_A)
class _AlAddressStatsHeldTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlAddressStatsHeldTimeLeft_Type.__name__=_D
_AlAddressStatsHeldTimeLeft_Object=MibTableColumn
alAddressStatsHeldTimeLeft=_AlAddressStatsHeldTimeLeft_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1,4),_AlAddressStatsHeldTimeLeft_Type())
alAddressStatsHeldTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldTimeLeft.setStatus(_A)
if mibBuilder.loadTexts:alAddressStatsHeldTimeLeft.setUnits(_N)
_AlAddressStatsHeldReason_Type=IPAddressHeldReason
_AlAddressStatsHeldReason_Object=MibTableColumn
alAddressStatsHeldReason=_AlAddressStatsHeldReason_Object((1,3,6,1,4,1,3076,2,1,2,19,4,1,5),_AlAddressStatsHeldReason_Type())
alAddressStatsHeldReason.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsHeldReason.setStatus(_A)
_AlAddressStatsGrpHeldTable_Object=MibTable
alAddressStatsGrpHeldTable=_AlAddressStatsGrpHeldTable_Object((1,3,6,1,4,1,3076,2,1,2,19,5))
if mibBuilder.loadTexts:alAddressStatsGrpHeldTable.setStatus(_A)
_AlAddressStatsGrpHeldEntry_Object=MibTableRow
alAddressStatsGrpHeldEntry=_AlAddressStatsGrpHeldEntry_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1))
alAddressStatsGrpHeldEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:alAddressStatsGrpHeldEntry.setStatus(_A)
class _AlAddressStatsGrpHeldId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpHeldId_Type.__name__=_D
_AlAddressStatsGrpHeldId_Object=MibTableColumn
alAddressStatsGrpHeldId=_AlAddressStatsGrpHeldId_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,1),_AlAddressStatsGrpHeldId_Type())
alAddressStatsGrpHeldId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldId.setStatus(_A)
class _AlAddressStatsGrpHeldPoolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpHeldPoolId_Type.__name__=_D
_AlAddressStatsGrpHeldPoolId_Object=MibTableColumn
alAddressStatsGrpHeldPoolId=_AlAddressStatsGrpHeldPoolId_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,2),_AlAddressStatsGrpHeldPoolId_Type())
alAddressStatsGrpHeldPoolId.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldPoolId.setStatus(_A)
class _AlAddressStatsGrpHeldAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlAddressStatsGrpHeldAddrIndex_Type.__name__=_D
_AlAddressStatsGrpHeldAddrIndex_Object=MibTableColumn
alAddressStatsGrpHeldAddrIndex=_AlAddressStatsGrpHeldAddrIndex_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,3),_AlAddressStatsGrpHeldAddrIndex_Type())
alAddressStatsGrpHeldAddrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldAddrIndex.setStatus(_A)
_AlAddressStatsGrpHeldAddress_Type=IpAddress
_AlAddressStatsGrpHeldAddress_Object=MibTableColumn
alAddressStatsGrpHeldAddress=_AlAddressStatsGrpHeldAddress_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,4),_AlAddressStatsGrpHeldAddress_Type())
alAddressStatsGrpHeldAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldAddress.setStatus(_A)
class _AlAddressStatsGrpHeldTimeLeft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlAddressStatsGrpHeldTimeLeft_Type.__name__=_D
_AlAddressStatsGrpHeldTimeLeft_Object=MibTableColumn
alAddressStatsGrpHeldTimeLeft=_AlAddressStatsGrpHeldTimeLeft_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,5),_AlAddressStatsGrpHeldTimeLeft_Type())
alAddressStatsGrpHeldTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldTimeLeft.setStatus(_A)
if mibBuilder.loadTexts:alAddressStatsGrpHeldTimeLeft.setUnits(_N)
_AlAddressStatsGrpHeldReason_Type=IPAddressHeldReason
_AlAddressStatsGrpHeldReason_Object=MibTableColumn
alAddressStatsGrpHeldReason=_AlAddressStatsGrpHeldReason_Object((1,3,6,1,4,1,3076,2,1,2,19,5,1,6),_AlAddressStatsGrpHeldReason_Type())
alAddressStatsGrpHeldReason.setMaxAccess(_C)
if mibBuilder.loadTexts:alAddressStatsGrpHeldReason.setStatus(_A)
altigaAddressStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,19,2))
altigaAddressStatsGroup.setObjects(*((_B,_E),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_F),(_B,_G),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:altigaAddressStatsGroup.setStatus(_A)
altigaAddressStatsGroupSup1=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,19,3))
altigaAddressStatsGroupSup1.setObjects(*((_B,_W),(_B,_X),(_B,_H),(_B,_I),(_B,_Y),(_B,_Z),(_B,_a),(_B,_J),(_B,_K),(_B,_L),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:altigaAddressStatsGroupSup1.setStatus(_A)
altigaAddressStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,24,2,1,1,1))
altigaAddressStatsMibCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:altigaAddressStatsMibCompliance.setStatus('deprecated')
altigaAddressStatsMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,3076,1,1,24,2,1,1,2))
altigaAddressStatsMibComplianceRev1.setObjects(*((_B,_M),(_B,_e)))
if mibBuilder.loadTexts:altigaAddressStatsMibComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IPAddressHeldReason':IPAddressHeldReason,'altigaAddressStatsMibModule':altigaAddressStatsMibModule,'altigaAddressStatsMibConformance':altigaAddressStatsMibConformance,'altigaAddressStatsMibCompliances':altigaAddressStatsMibCompliances,'altigaAddressStatsMibCompliance':altigaAddressStatsMibCompliance,'altigaAddressStatsMibComplianceRev1':altigaAddressStatsMibComplianceRev1,_M:altigaAddressStatsGroup,_e:altigaAddressStatsGroupSup1,'alAddressStatsGlobal':alAddressStatsGlobal,'alAddressStatsPoolTable':alAddressStatsPoolTable,'alAddressStatsPoolEntry':alAddressStatsPoolEntry,_E:alAddressStatsPoolId,_O:alAddressStatsTotalPoolAddresses,_P:alAddressStatsCurrAllocAddresses,_Q:alAddressStatsCurrAvailAddresses,_R:alAddressStatsMaxAddressesAssigned,_W:alAddressStatsHeldAddresses,'alAddressStatsPoolGroupTable':alAddressStatsPoolGroupTable,'alAddressStatsPoolGroupEntry':alAddressStatsPoolGroupEntry,_F:alAddressStatsGrpId,_G:alAddressStatsGrpPoolId,_S:alAddressStatsGrpTotalPoolAddresses,_T:alAddressStatsGrpCurrAllocAddresses,_U:alAddressStatsGrpCurrAvailAddresses,_V:alAddressStatsGrpMaxAddressesAssigned,_X:alAddressStatsGrpHeldAddresses,'alAddressStatsHeldTable':alAddressStatsHeldTable,'alAddressStatsHeldEntry':alAddressStatsHeldEntry,_H:alAddressStatsHeldPoolId,_I:alAddressStatsHeldAddrIndex,_Y:alAddressStatsHeldAddress,_Z:alAddressStatsHeldTimeLeft,_a:alAddressStatsHeldReason,'alAddressStatsGrpHeldTable':alAddressStatsGrpHeldTable,'alAddressStatsGrpHeldEntry':alAddressStatsGrpHeldEntry,_J:alAddressStatsGrpHeldId,_K:alAddressStatsGrpHeldPoolId,_L:alAddressStatsGrpHeldAddrIndex,_b:alAddressStatsGrpHeldAddress,_c:alAddressStatsGrpHeldTimeLeft,_d:alAddressStatsGrpHeldReason})