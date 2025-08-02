_i='ciscoGactGttGroupRev1'
_h='ciscoGactGttGroup'
_g='cgactGtt2Octets'
_f='cgactGtt2Packets'
_e='cgactGttOctets'
_d='cgactGttPackets'
_c='cgactMtp3OutOctets'
_b='cgactMtp3InOctets'
_a='cgactMtp3OutPackets'
_Z='cgactMtp3InPackets'
_Y='cgactGtt2TranslatedPc'
_X='cgactGtt2TranslatedInstNumber'
_W='cgactGtt2Gta'
_V='cgactGtt2SelectorName'
_U='cgactGtt2LinksetName'
_T='cgactGttTranslatedPc'
_S='cgactGttGta'
_R='cgactGttSelectorName'
_Q='cgactGttLinksetName'
_P='cgactMtp3SI'
_O='cgactMtp3Opc'
_N='cgactMtp3Dpc'
_M='cgactMtp3LinksetName'
_L='cgactMtp3TableId'
_K='Integer32'
_J='ciscoGactMtp3Group'
_I='octets'
_H='packets'
_G='cgspInstNetwork'
_F='CISCO-ITP-GSP-MIB'
_E='read-only'
_D='deprecated'
_C='not-accessible'
_B='current'
_A='CISCO-ITP-GACT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgspInstNetwork,=mibBuilder.importSymbols(_F,_G)
CItpTcGlobalTitleSelectorName,CItpTcGtaLongAddr,CItpTcInstanceNumber,CItpTcLinksetId,CItpTcPointCode,CItpTcServiceIndicator=mibBuilder.importSymbols('CISCO-ITP-TC-MIB','CItpTcGlobalTitleSelectorName','CItpTcGtaLongAddr','CItpTcInstanceNumber','CItpTcLinksetId','CItpTcPointCode','CItpTcServiceIndicator')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoGactMIB=ModuleIdentity((1,3,6,1,4,1,9,9,333))
if mibBuilder.loadTexts:ciscoGactMIB.setRevisions(('2003-10-01 00:00','2003-03-03 00:00'))
_CgactMIBNotifs_ObjectIdentity=ObjectIdentity
cgactMIBNotifs=_CgactMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,333,0))
_CgactMIBObjects_ObjectIdentity=ObjectIdentity
cgactMIBObjects=_CgactMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,333,1))
_CgactMtp3_ObjectIdentity=ObjectIdentity
cgactMtp3=_CgactMtp3_ObjectIdentity((1,3,6,1,4,1,9,9,333,1,1))
_CgactMtp3Table_Object=MibTable
cgactMtp3Table=_CgactMtp3Table_Object((1,3,6,1,4,1,9,9,333,1,1,1))
if mibBuilder.loadTexts:cgactMtp3Table.setStatus(_B)
_CgactMtp3TableEntry_Object=MibTableRow
cgactMtp3TableEntry=_CgactMtp3TableEntry_Object((1,3,6,1,4,1,9,9,333,1,1,1,1))
cgactMtp3TableEntry.setIndexNames((0,_F,_G),(0,_A,_L),(0,_A,_M),(0,_A,_N),(0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:cgactMtp3TableEntry.setStatus(_B)
class _CgactMtp3TableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('passed',1),('violation',2),('unroutable',3)))
_CgactMtp3TableId_Type.__name__=_K
_CgactMtp3TableId_Object=MibTableColumn
cgactMtp3TableId=_CgactMtp3TableId_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,1),_CgactMtp3TableId_Type())
cgactMtp3TableId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactMtp3TableId.setStatus(_B)
_CgactMtp3LinksetName_Type=CItpTcLinksetId
_CgactMtp3LinksetName_Object=MibTableColumn
cgactMtp3LinksetName=_CgactMtp3LinksetName_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,2),_CgactMtp3LinksetName_Type())
cgactMtp3LinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactMtp3LinksetName.setStatus(_B)
_CgactMtp3Dpc_Type=CItpTcPointCode
_CgactMtp3Dpc_Object=MibTableColumn
cgactMtp3Dpc=_CgactMtp3Dpc_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,3),_CgactMtp3Dpc_Type())
cgactMtp3Dpc.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactMtp3Dpc.setStatus(_B)
_CgactMtp3Opc_Type=CItpTcPointCode
_CgactMtp3Opc_Object=MibTableColumn
cgactMtp3Opc=_CgactMtp3Opc_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,4),_CgactMtp3Opc_Type())
cgactMtp3Opc.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactMtp3Opc.setStatus(_B)
_CgactMtp3SI_Type=CItpTcServiceIndicator
_CgactMtp3SI_Object=MibTableColumn
cgactMtp3SI=_CgactMtp3SI_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,5),_CgactMtp3SI_Type())
cgactMtp3SI.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactMtp3SI.setStatus(_B)
_CgactMtp3InPackets_Type=Counter32
_CgactMtp3InPackets_Object=MibTableColumn
cgactMtp3InPackets=_CgactMtp3InPackets_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,6),_CgactMtp3InPackets_Type())
cgactMtp3InPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactMtp3InPackets.setStatus(_B)
if mibBuilder.loadTexts:cgactMtp3InPackets.setUnits(_H)
_CgactMtp3OutPackets_Type=Counter32
_CgactMtp3OutPackets_Object=MibTableColumn
cgactMtp3OutPackets=_CgactMtp3OutPackets_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,7),_CgactMtp3OutPackets_Type())
cgactMtp3OutPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactMtp3OutPackets.setStatus(_B)
if mibBuilder.loadTexts:cgactMtp3OutPackets.setUnits(_H)
_CgactMtp3InOctets_Type=Counter32
_CgactMtp3InOctets_Object=MibTableColumn
cgactMtp3InOctets=_CgactMtp3InOctets_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,8),_CgactMtp3InOctets_Type())
cgactMtp3InOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactMtp3InOctets.setStatus(_B)
if mibBuilder.loadTexts:cgactMtp3InOctets.setUnits(_I)
_CgactMtp3OutOctets_Type=Counter32
_CgactMtp3OutOctets_Object=MibTableColumn
cgactMtp3OutOctets=_CgactMtp3OutOctets_Object((1,3,6,1,4,1,9,9,333,1,1,1,1,9),_CgactMtp3OutOctets_Type())
cgactMtp3OutOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactMtp3OutOctets.setStatus(_B)
if mibBuilder.loadTexts:cgactMtp3OutOctets.setUnits(_I)
_CgactGtt_ObjectIdentity=ObjectIdentity
cgactGtt=_CgactGtt_ObjectIdentity((1,3,6,1,4,1,9,9,333,1,2))
_CgactGttTable_Object=MibTable
cgactGttTable=_CgactGttTable_Object((1,3,6,1,4,1,9,9,333,1,2,1))
if mibBuilder.loadTexts:cgactGttTable.setStatus(_D)
_CgactGttTableEntry_Object=MibTableRow
cgactGttTableEntry=_CgactGttTableEntry_Object((1,3,6,1,4,1,9,9,333,1,2,1,1))
cgactGttTableEntry.setIndexNames((0,_F,_G),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:cgactGttTableEntry.setStatus(_D)
_CgactGttLinksetName_Type=CItpTcLinksetId
_CgactGttLinksetName_Object=MibTableColumn
cgactGttLinksetName=_CgactGttLinksetName_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,1),_CgactGttLinksetName_Type())
cgactGttLinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGttLinksetName.setStatus(_D)
_CgactGttSelectorName_Type=CItpTcGlobalTitleSelectorName
_CgactGttSelectorName_Object=MibTableColumn
cgactGttSelectorName=_CgactGttSelectorName_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,2),_CgactGttSelectorName_Type())
cgactGttSelectorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGttSelectorName.setStatus(_D)
_CgactGttGta_Type=CItpTcGtaLongAddr
_CgactGttGta_Object=MibTableColumn
cgactGttGta=_CgactGttGta_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,3),_CgactGttGta_Type())
cgactGttGta.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGttGta.setStatus(_D)
_CgactGttTranslatedPc_Type=CItpTcPointCode
_CgactGttTranslatedPc_Object=MibTableColumn
cgactGttTranslatedPc=_CgactGttTranslatedPc_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,4),_CgactGttTranslatedPc_Type())
cgactGttTranslatedPc.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGttTranslatedPc.setStatus(_D)
_CgactGttPackets_Type=Counter32
_CgactGttPackets_Object=MibTableColumn
cgactGttPackets=_CgactGttPackets_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,5),_CgactGttPackets_Type())
cgactGttPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactGttPackets.setStatus(_D)
if mibBuilder.loadTexts:cgactGttPackets.setUnits(_H)
_CgactGttOctets_Type=Counter32
_CgactGttOctets_Object=MibTableColumn
cgactGttOctets=_CgactGttOctets_Object((1,3,6,1,4,1,9,9,333,1,2,1,1,6),_CgactGttOctets_Type())
cgactGttOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactGttOctets.setStatus(_D)
if mibBuilder.loadTexts:cgactGttOctets.setUnits(_I)
_CgactGtt2Table_Object=MibTable
cgactGtt2Table=_CgactGtt2Table_Object((1,3,6,1,4,1,9,9,333,1,2,2))
if mibBuilder.loadTexts:cgactGtt2Table.setStatus(_B)
_CgactGtt2TableEntry_Object=MibTableRow
cgactGtt2TableEntry=_CgactGtt2TableEntry_Object((1,3,6,1,4,1,9,9,333,1,2,2,1))
cgactGtt2TableEntry.setIndexNames((0,_F,_G),(0,_A,_U),(0,_A,_V),(0,_A,_W),(0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:cgactGtt2TableEntry.setStatus(_B)
_CgactGtt2LinksetName_Type=CItpTcLinksetId
_CgactGtt2LinksetName_Object=MibTableColumn
cgactGtt2LinksetName=_CgactGtt2LinksetName_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,1),_CgactGtt2LinksetName_Type())
cgactGtt2LinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGtt2LinksetName.setStatus(_B)
_CgactGtt2SelectorName_Type=CItpTcGlobalTitleSelectorName
_CgactGtt2SelectorName_Object=MibTableColumn
cgactGtt2SelectorName=_CgactGtt2SelectorName_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,2),_CgactGtt2SelectorName_Type())
cgactGtt2SelectorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGtt2SelectorName.setStatus(_B)
_CgactGtt2Gta_Type=CItpTcGtaLongAddr
_CgactGtt2Gta_Object=MibTableColumn
cgactGtt2Gta=_CgactGtt2Gta_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,3),_CgactGtt2Gta_Type())
cgactGtt2Gta.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGtt2Gta.setStatus(_B)
_CgactGtt2TranslatedInstNumber_Type=CItpTcInstanceNumber
_CgactGtt2TranslatedInstNumber_Object=MibTableColumn
cgactGtt2TranslatedInstNumber=_CgactGtt2TranslatedInstNumber_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,4),_CgactGtt2TranslatedInstNumber_Type())
cgactGtt2TranslatedInstNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGtt2TranslatedInstNumber.setStatus(_B)
_CgactGtt2TranslatedPc_Type=CItpTcPointCode
_CgactGtt2TranslatedPc_Object=MibTableColumn
cgactGtt2TranslatedPc=_CgactGtt2TranslatedPc_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,5),_CgactGtt2TranslatedPc_Type())
cgactGtt2TranslatedPc.setMaxAccess(_C)
if mibBuilder.loadTexts:cgactGtt2TranslatedPc.setStatus(_B)
_CgactGtt2Packets_Type=Counter32
_CgactGtt2Packets_Object=MibTableColumn
cgactGtt2Packets=_CgactGtt2Packets_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,6),_CgactGtt2Packets_Type())
cgactGtt2Packets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactGtt2Packets.setStatus(_B)
if mibBuilder.loadTexts:cgactGtt2Packets.setUnits(_H)
_CgactGtt2Octets_Type=Counter32
_CgactGtt2Octets_Object=MibTableColumn
cgactGtt2Octets=_CgactGtt2Octets_Object((1,3,6,1,4,1,9,9,333,1,2,2,1,7),_CgactGtt2Octets_Type())
cgactGtt2Octets.setMaxAccess(_E)
if mibBuilder.loadTexts:cgactGtt2Octets.setStatus(_B)
if mibBuilder.loadTexts:cgactGtt2Octets.setUnits(_I)
_CgactMIBConform_ObjectIdentity=ObjectIdentity
cgactMIBConform=_CgactMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,333,2))
_CiscoGactMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGactMIBCompliances=_CiscoGactMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,333,2,1))
_CiscoGactMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGactMIBGroups=_CiscoGactMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,333,2,2))
ciscoGactMtp3Group=ObjectGroup((1,3,6,1,4,1,9,9,333,2,2,1))
ciscoGactMtp3Group.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoGactMtp3Group.setStatus(_B)
ciscoGactGttGroup=ObjectGroup((1,3,6,1,4,1,9,9,333,2,2,2))
ciscoGactGttGroup.setObjects(*((_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoGactGttGroup.setStatus(_D)
ciscoGactGttGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,333,2,2,3))
ciscoGactGttGroupRev1.setObjects(*((_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoGactGttGroupRev1.setStatus(_B)
ciscoGactMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,333,2,1,1))
ciscoGactMIBCompliance.setObjects(*((_A,_J),(_A,_h)))
if mibBuilder.loadTexts:ciscoGactMIBCompliance.setStatus(_D)
ciscoGactMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,333,2,1,2))
ciscoGactMIBComplianceRev1.setObjects(*((_A,_J),(_A,_i)))
if mibBuilder.loadTexts:ciscoGactMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoGactMIB':ciscoGactMIB,'cgactMIBNotifs':cgactMIBNotifs,'cgactMIBObjects':cgactMIBObjects,'cgactMtp3':cgactMtp3,'cgactMtp3Table':cgactMtp3Table,'cgactMtp3TableEntry':cgactMtp3TableEntry,_L:cgactMtp3TableId,_M:cgactMtp3LinksetName,_N:cgactMtp3Dpc,_O:cgactMtp3Opc,_P:cgactMtp3SI,_Z:cgactMtp3InPackets,_a:cgactMtp3OutPackets,_b:cgactMtp3InOctets,_c:cgactMtp3OutOctets,'cgactGtt':cgactGtt,'cgactGttTable':cgactGttTable,'cgactGttTableEntry':cgactGttTableEntry,_Q:cgactGttLinksetName,_R:cgactGttSelectorName,_S:cgactGttGta,_T:cgactGttTranslatedPc,_d:cgactGttPackets,_e:cgactGttOctets,'cgactGtt2Table':cgactGtt2Table,'cgactGtt2TableEntry':cgactGtt2TableEntry,_U:cgactGtt2LinksetName,_V:cgactGtt2SelectorName,_W:cgactGtt2Gta,_X:cgactGtt2TranslatedInstNumber,_Y:cgactGtt2TranslatedPc,_f:cgactGtt2Packets,_g:cgactGtt2Octets,'cgactMIBConform':cgactMIBConform,'ciscoGactMIBCompliances':ciscoGactMIBCompliances,'ciscoGactMIBCompliance':ciscoGactMIBCompliance,'ciscoGactMIBComplianceRev1':ciscoGactMIBComplianceRev1,'ciscoGactMIBGroups':ciscoGactMIBGroups,_J:ciscoGactMtp3Group,_h:ciscoGactGttGroup,_i:ciscoGactGttGroupRev1})