_d='cHsrpExtIfTrackedGroupSup1'
_c='cHsrpExtIfTrackedIpNone'
_b='cHsrpExtIfStandbyRowStatus'
_a='cHsrpExtIfStandbySourceAddr'
_Z='cHsrpExtIfStandbySourceAddrType'
_Y='cHsrpExtIfStandbyDestAddr'
_X='cHsrpExtIfStandbyDestAddrType'
_W='cHsrpExtIfRowStatus'
_V='cHsrpExtIfUseBIA'
_U='cHsrpExtSecAddrRowStatus'
_T='cHsrpExtIfTrackedRowStatus'
_S='cHsrpExtIfTrackedPriority'
_R='cHsrpExtIfStandbyIndex'
_Q='cHsrpExtSecAddrAddress'
_P='cHsrpExtIfTracked'
_O='cHsrpExtIfStandbyGroup91'
_N='not-accessible'
_M='TruthValue'
_L='Unsigned32'
_K='cHsrpExtIfGroup'
_J='cHsrpExtSecAddrGroup'
_I='cHsrpExtIfTrackedGroup'
_H='deprecated'
_G='cHsrpGrpNumber'
_F='CISCO-HSRP-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='read-create'
_B='current'
_A='CISCO-HSRP-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cHsrpGrpNumber,=mibBuilder.importSymbols(_F,_G)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex',_E)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
ciscoHsrpExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,107))
if mibBuilder.loadTexts:ciscoHsrpExtMIB.setRevisions(('2010-09-02 00:00','2010-02-05 00:00','2006-02-15 00:00','1998-08-03 00:00'))
_CiscoHsrpExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoHsrpExtMIBObjects=_CiscoHsrpExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,107,1))
_CHsrpExtGroup_ObjectIdentity=ObjectIdentity
cHsrpExtGroup=_CHsrpExtGroup_ObjectIdentity((1,3,6,1,4,1,9,9,107,1,1))
_CHsrpExtIfTrackedTable_Object=MibTable
cHsrpExtIfTrackedTable=_CHsrpExtIfTrackedTable_Object((1,3,6,1,4,1,9,9,107,1,1,1))
if mibBuilder.loadTexts:cHsrpExtIfTrackedTable.setStatus(_B)
_CHsrpExtIfTrackedEntry_Object=MibTableRow
cHsrpExtIfTrackedEntry=_CHsrpExtIfTrackedEntry_Object((1,3,6,1,4,1,9,9,107,1,1,1,1))
cHsrpExtIfTrackedEntry.setIndexNames((0,_D,_E),(0,_F,_G),(0,_A,_P))
if mibBuilder.loadTexts:cHsrpExtIfTrackedEntry.setStatus(_B)
_CHsrpExtIfTracked_Type=InterfaceIndex
_CHsrpExtIfTracked_Object=MibTableColumn
cHsrpExtIfTracked=_CHsrpExtIfTracked_Object((1,3,6,1,4,1,9,9,107,1,1,1,1,1),_CHsrpExtIfTracked_Type())
cHsrpExtIfTracked.setMaxAccess(_N)
if mibBuilder.loadTexts:cHsrpExtIfTracked.setStatus(_B)
class _CHsrpExtIfTrackedPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CHsrpExtIfTrackedPriority_Type.__name__=_L
_CHsrpExtIfTrackedPriority_Object=MibTableColumn
cHsrpExtIfTrackedPriority=_CHsrpExtIfTrackedPriority_Object((1,3,6,1,4,1,9,9,107,1,1,1,1,2),_CHsrpExtIfTrackedPriority_Type())
cHsrpExtIfTrackedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfTrackedPriority.setStatus(_B)
_CHsrpExtIfTrackedRowStatus_Type=RowStatus
_CHsrpExtIfTrackedRowStatus_Object=MibTableColumn
cHsrpExtIfTrackedRowStatus=_CHsrpExtIfTrackedRowStatus_Object((1,3,6,1,4,1,9,9,107,1,1,1,1,3),_CHsrpExtIfTrackedRowStatus_Type())
cHsrpExtIfTrackedRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfTrackedRowStatus.setStatus(_B)
class _CHsrpExtIfTrackedIpNone_Type(TruthValue):defaultValue=2
_CHsrpExtIfTrackedIpNone_Type.__name__=_M
_CHsrpExtIfTrackedIpNone_Object=MibTableColumn
cHsrpExtIfTrackedIpNone=_CHsrpExtIfTrackedIpNone_Object((1,3,6,1,4,1,9,9,107,1,1,1,1,4),_CHsrpExtIfTrackedIpNone_Type())
cHsrpExtIfTrackedIpNone.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfTrackedIpNone.setStatus(_H)
_CHsrpExtSecAddrTable_Object=MibTable
cHsrpExtSecAddrTable=_CHsrpExtSecAddrTable_Object((1,3,6,1,4,1,9,9,107,1,1,2))
if mibBuilder.loadTexts:cHsrpExtSecAddrTable.setStatus(_B)
_CHsrpExtSecAddrEntry_Object=MibTableRow
cHsrpExtSecAddrEntry=_CHsrpExtSecAddrEntry_Object((1,3,6,1,4,1,9,9,107,1,1,2,1))
cHsrpExtSecAddrEntry.setIndexNames((0,_D,_E),(0,_F,_G),(0,_A,_Q))
if mibBuilder.loadTexts:cHsrpExtSecAddrEntry.setStatus(_B)
_CHsrpExtSecAddrAddress_Type=IpAddress
_CHsrpExtSecAddrAddress_Object=MibTableColumn
cHsrpExtSecAddrAddress=_CHsrpExtSecAddrAddress_Object((1,3,6,1,4,1,9,9,107,1,1,2,1,1),_CHsrpExtSecAddrAddress_Type())
cHsrpExtSecAddrAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:cHsrpExtSecAddrAddress.setStatus(_B)
_CHsrpExtSecAddrRowStatus_Type=RowStatus
_CHsrpExtSecAddrRowStatus_Object=MibTableColumn
cHsrpExtSecAddrRowStatus=_CHsrpExtSecAddrRowStatus_Object((1,3,6,1,4,1,9,9,107,1,1,2,1,2),_CHsrpExtSecAddrRowStatus_Type())
cHsrpExtSecAddrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtSecAddrRowStatus.setStatus(_B)
_CHsrpExtIfStandbyTable_Object=MibTable
cHsrpExtIfStandbyTable=_CHsrpExtIfStandbyTable_Object((1,3,6,1,4,1,9,9,107,1,1,3))
if mibBuilder.loadTexts:cHsrpExtIfStandbyTable.setStatus(_B)
_CHsrpExtIfStandbyEntry_Object=MibTableRow
cHsrpExtIfStandbyEntry=_CHsrpExtIfStandbyEntry_Object((1,3,6,1,4,1,9,9,107,1,1,3,1))
cHsrpExtIfStandbyEntry.setIndexNames((0,_D,_E),(0,_F,_G),(0,_A,_R))
if mibBuilder.loadTexts:cHsrpExtIfStandbyEntry.setStatus(_B)
class _CHsrpExtIfStandbyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CHsrpExtIfStandbyIndex_Type.__name__=_L
_CHsrpExtIfStandbyIndex_Object=MibTableColumn
cHsrpExtIfStandbyIndex=_CHsrpExtIfStandbyIndex_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,1),_CHsrpExtIfStandbyIndex_Type())
cHsrpExtIfStandbyIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cHsrpExtIfStandbyIndex.setStatus(_B)
_CHsrpExtIfStandbyDestAddrType_Type=InetAddressType
_CHsrpExtIfStandbyDestAddrType_Object=MibTableColumn
cHsrpExtIfStandbyDestAddrType=_CHsrpExtIfStandbyDestAddrType_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,2),_CHsrpExtIfStandbyDestAddrType_Type())
cHsrpExtIfStandbyDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfStandbyDestAddrType.setStatus(_B)
_CHsrpExtIfStandbyDestAddr_Type=InetAddress
_CHsrpExtIfStandbyDestAddr_Object=MibTableColumn
cHsrpExtIfStandbyDestAddr=_CHsrpExtIfStandbyDestAddr_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,3),_CHsrpExtIfStandbyDestAddr_Type())
cHsrpExtIfStandbyDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfStandbyDestAddr.setStatus(_B)
_CHsrpExtIfStandbySourceAddrType_Type=InetAddressType
_CHsrpExtIfStandbySourceAddrType_Object=MibTableColumn
cHsrpExtIfStandbySourceAddrType=_CHsrpExtIfStandbySourceAddrType_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,4),_CHsrpExtIfStandbySourceAddrType_Type())
cHsrpExtIfStandbySourceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfStandbySourceAddrType.setStatus(_B)
_CHsrpExtIfStandbySourceAddr_Type=InetAddress
_CHsrpExtIfStandbySourceAddr_Object=MibTableColumn
cHsrpExtIfStandbySourceAddr=_CHsrpExtIfStandbySourceAddr_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,5),_CHsrpExtIfStandbySourceAddr_Type())
cHsrpExtIfStandbySourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfStandbySourceAddr.setStatus(_B)
_CHsrpExtIfStandbyRowStatus_Type=RowStatus
_CHsrpExtIfStandbyRowStatus_Object=MibTableColumn
cHsrpExtIfStandbyRowStatus=_CHsrpExtIfStandbyRowStatus_Object((1,3,6,1,4,1,9,9,107,1,1,3,1,6),_CHsrpExtIfStandbyRowStatus_Type())
cHsrpExtIfStandbyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfStandbyRowStatus.setStatus(_B)
_CHsrpExtIfBIA_ObjectIdentity=ObjectIdentity
cHsrpExtIfBIA=_CHsrpExtIfBIA_ObjectIdentity((1,3,6,1,4,1,9,9,107,1,2))
_CHsrpExtIfTable_Object=MibTable
cHsrpExtIfTable=_CHsrpExtIfTable_Object((1,3,6,1,4,1,9,9,107,1,2,1))
if mibBuilder.loadTexts:cHsrpExtIfTable.setStatus(_B)
_CHsrpExtIfEntry_Object=MibTableRow
cHsrpExtIfEntry=_CHsrpExtIfEntry_Object((1,3,6,1,4,1,9,9,107,1,2,1,1))
cHsrpExtIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cHsrpExtIfEntry.setStatus(_B)
class _CHsrpExtIfUseBIA_Type(TruthValue):defaultValue=2
_CHsrpExtIfUseBIA_Type.__name__=_M
_CHsrpExtIfUseBIA_Object=MibTableColumn
cHsrpExtIfUseBIA=_CHsrpExtIfUseBIA_Object((1,3,6,1,4,1,9,9,107,1,2,1,1,1),_CHsrpExtIfUseBIA_Type())
cHsrpExtIfUseBIA.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfUseBIA.setStatus(_B)
_CHsrpExtIfRowStatus_Type=RowStatus
_CHsrpExtIfRowStatus_Object=MibTableColumn
cHsrpExtIfRowStatus=_CHsrpExtIfRowStatus_Object((1,3,6,1,4,1,9,9,107,1,2,1,1,2),_CHsrpExtIfRowStatus_Type())
cHsrpExtIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cHsrpExtIfRowStatus.setStatus(_B)
_CHsrpExtConformance_ObjectIdentity=ObjectIdentity
cHsrpExtConformance=_CHsrpExtConformance_ObjectIdentity((1,3,6,1,4,1,9,9,107,3))
_CHsrpExtCompliances_ObjectIdentity=ObjectIdentity
cHsrpExtCompliances=_CHsrpExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,107,3,1))
_CHsrpExtComplianceGroups_ObjectIdentity=ObjectIdentity
cHsrpExtComplianceGroups=_CHsrpExtComplianceGroups_ObjectIdentity((1,3,6,1,4,1,9,9,107,3,2))
cHsrpExtIfTrackedGroup=ObjectGroup((1,3,6,1,4,1,9,9,107,3,2,1))
cHsrpExtIfTrackedGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cHsrpExtIfTrackedGroup.setStatus(_B)
cHsrpExtSecAddrGroup=ObjectGroup((1,3,6,1,4,1,9,9,107,3,2,2))
cHsrpExtSecAddrGroup.setObjects((_A,_U))
if mibBuilder.loadTexts:cHsrpExtSecAddrGroup.setStatus(_B)
cHsrpExtIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,107,3,2,3))
cHsrpExtIfGroup.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cHsrpExtIfGroup.setStatus(_B)
cHsrpExtIfStandbyGroup91=ObjectGroup((1,3,6,1,4,1,9,9,107,3,2,4))
cHsrpExtIfStandbyGroup91.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cHsrpExtIfStandbyGroup91.setStatus(_B)
cHsrpExtIfTrackedGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,107,3,2,5))
cHsrpExtIfTrackedGroupSup1.setObjects((_A,_c))
if mibBuilder.loadTexts:cHsrpExtIfTrackedGroupSup1.setStatus(_H)
cHsrpExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,107,3,1,1))
cHsrpExtCompliance.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cHsrpExtCompliance.setStatus(_H)
cHsrpExtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,107,3,1,2))
cHsrpExtComplianceRev1.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_O),(_A,_d)))
if mibBuilder.loadTexts:cHsrpExtComplianceRev1.setStatus(_H)
cHsrpExtComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,107,3,1,3))
cHsrpExtComplianceRev2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_O)))
if mibBuilder.loadTexts:cHsrpExtComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoHsrpExtMIB':ciscoHsrpExtMIB,'ciscoHsrpExtMIBObjects':ciscoHsrpExtMIBObjects,'cHsrpExtGroup':cHsrpExtGroup,'cHsrpExtIfTrackedTable':cHsrpExtIfTrackedTable,'cHsrpExtIfTrackedEntry':cHsrpExtIfTrackedEntry,_P:cHsrpExtIfTracked,_S:cHsrpExtIfTrackedPriority,_T:cHsrpExtIfTrackedRowStatus,_c:cHsrpExtIfTrackedIpNone,'cHsrpExtSecAddrTable':cHsrpExtSecAddrTable,'cHsrpExtSecAddrEntry':cHsrpExtSecAddrEntry,_Q:cHsrpExtSecAddrAddress,_U:cHsrpExtSecAddrRowStatus,'cHsrpExtIfStandbyTable':cHsrpExtIfStandbyTable,'cHsrpExtIfStandbyEntry':cHsrpExtIfStandbyEntry,_R:cHsrpExtIfStandbyIndex,_X:cHsrpExtIfStandbyDestAddrType,_Y:cHsrpExtIfStandbyDestAddr,_Z:cHsrpExtIfStandbySourceAddrType,_a:cHsrpExtIfStandbySourceAddr,_b:cHsrpExtIfStandbyRowStatus,'cHsrpExtIfBIA':cHsrpExtIfBIA,'cHsrpExtIfTable':cHsrpExtIfTable,'cHsrpExtIfEntry':cHsrpExtIfEntry,_V:cHsrpExtIfUseBIA,_W:cHsrpExtIfRowStatus,'cHsrpExtConformance':cHsrpExtConformance,'cHsrpExtCompliances':cHsrpExtCompliances,'cHsrpExtCompliance':cHsrpExtCompliance,'cHsrpExtComplianceRev1':cHsrpExtComplianceRev1,'cHsrpExtComplianceRev2':cHsrpExtComplianceRev2,'cHsrpExtComplianceGroups':cHsrpExtComplianceGroups,_I:cHsrpExtIfTrackedGroup,_J:cHsrpExtSecAddrGroup,_K:cHsrpExtIfGroup,_O:cHsrpExtIfStandbyGroup91,_d:cHsrpExtIfTrackedGroupSup1})