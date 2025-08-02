_X='cItpActGttGroup'
_W='cItpActMtp3Group'
_V='cItpActGttBytes'
_U='cItpActGttPackets'
_T='cItpActMtp3SentBytes'
_S='cItpActMtp3RcvdBytes'
_R='cItpActMtp3SentPackets'
_Q='cItpActMtp3RcvdPackets'
_P='cItpActGttTranslatedPc'
_O='cItpActGttGta'
_N='cItpActGttSelectorName'
_M='cItpActGttLinksetName'
_L='packets'
_K='cItpActMtp3SI'
_J='cItpActMtp3Opc'
_I='cItpActMtp3Dpc'
_H='cItpActMtp3LinksetName'
_G='cItpActMtp3TableId'
_F='Integer32'
_E='bytes'
_D='read-only'
_C='not-accessible'
_B='CISCO-ITP-ACT-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CItpTcGlobalTitleSelectorName,CItpTcGtaAddr,CItpTcLinksetId,CItpTcPointCode,CItpTcServiceIndicator=mibBuilder.importSymbols('CISCO-ITP-TC-MIB','CItpTcGlobalTitleSelectorName','CItpTcGtaAddr','CItpTcLinksetId','CItpTcPointCode','CItpTcServiceIndicator')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoItpActMIB=ModuleIdentity((1,3,6,1,4,1,9,9,230))
if mibBuilder.loadTexts:ciscoItpActMIB.setRevisions(('2002-12-18 00:00','2001-09-26 00:00'))
_CItpActMIBNotifs_ObjectIdentity=ObjectIdentity
cItpActMIBNotifs=_CItpActMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,230,0))
_CItpActMIBObjects_ObjectIdentity=ObjectIdentity
cItpActMIBObjects=_CItpActMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,230,1))
_CItpActMtp3_ObjectIdentity=ObjectIdentity
cItpActMtp3=_CItpActMtp3_ObjectIdentity((1,3,6,1,4,1,9,9,230,1,1))
_CItpActMtp3Table_Object=MibTable
cItpActMtp3Table=_CItpActMtp3Table_Object((1,3,6,1,4,1,9,9,230,1,1,1))
if mibBuilder.loadTexts:cItpActMtp3Table.setStatus(_A)
_CItpActMtp3TableEntry_Object=MibTableRow
cItpActMtp3TableEntry=_CItpActMtp3TableEntry_Object((1,3,6,1,4,1,9,9,230,1,1,1,1))
cItpActMtp3TableEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cItpActMtp3TableEntry.setStatus(_A)
class _CItpActMtp3TableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passed',1),('violation',2)))
_CItpActMtp3TableId_Type.__name__=_F
_CItpActMtp3TableId_Object=MibTableColumn
cItpActMtp3TableId=_CItpActMtp3TableId_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,1),_CItpActMtp3TableId_Type())
cItpActMtp3TableId.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActMtp3TableId.setStatus(_A)
_CItpActMtp3LinksetName_Type=CItpTcLinksetId
_CItpActMtp3LinksetName_Object=MibTableColumn
cItpActMtp3LinksetName=_CItpActMtp3LinksetName_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,2),_CItpActMtp3LinksetName_Type())
cItpActMtp3LinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActMtp3LinksetName.setStatus(_A)
_CItpActMtp3Dpc_Type=CItpTcPointCode
_CItpActMtp3Dpc_Object=MibTableColumn
cItpActMtp3Dpc=_CItpActMtp3Dpc_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,3),_CItpActMtp3Dpc_Type())
cItpActMtp3Dpc.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActMtp3Dpc.setStatus(_A)
_CItpActMtp3Opc_Type=CItpTcPointCode
_CItpActMtp3Opc_Object=MibTableColumn
cItpActMtp3Opc=_CItpActMtp3Opc_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,4),_CItpActMtp3Opc_Type())
cItpActMtp3Opc.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActMtp3Opc.setStatus(_A)
_CItpActMtp3SI_Type=CItpTcServiceIndicator
_CItpActMtp3SI_Object=MibTableColumn
cItpActMtp3SI=_CItpActMtp3SI_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,5),_CItpActMtp3SI_Type())
cItpActMtp3SI.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActMtp3SI.setStatus(_A)
_CItpActMtp3RcvdPackets_Type=Counter32
_CItpActMtp3RcvdPackets_Object=MibTableColumn
cItpActMtp3RcvdPackets=_CItpActMtp3RcvdPackets_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,6),_CItpActMtp3RcvdPackets_Type())
cItpActMtp3RcvdPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActMtp3RcvdPackets.setStatus(_A)
if mibBuilder.loadTexts:cItpActMtp3RcvdPackets.setUnits(_L)
_CItpActMtp3SentPackets_Type=Counter32
_CItpActMtp3SentPackets_Object=MibTableColumn
cItpActMtp3SentPackets=_CItpActMtp3SentPackets_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,7),_CItpActMtp3SentPackets_Type())
cItpActMtp3SentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActMtp3SentPackets.setStatus(_A)
if mibBuilder.loadTexts:cItpActMtp3SentPackets.setUnits(_L)
_CItpActMtp3RcvdBytes_Type=Counter32
_CItpActMtp3RcvdBytes_Object=MibTableColumn
cItpActMtp3RcvdBytes=_CItpActMtp3RcvdBytes_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,8),_CItpActMtp3RcvdBytes_Type())
cItpActMtp3RcvdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActMtp3RcvdBytes.setStatus(_A)
if mibBuilder.loadTexts:cItpActMtp3RcvdBytes.setUnits(_E)
_CItpActMtp3SentBytes_Type=Counter32
_CItpActMtp3SentBytes_Object=MibTableColumn
cItpActMtp3SentBytes=_CItpActMtp3SentBytes_Object((1,3,6,1,4,1,9,9,230,1,1,1,1,9),_CItpActMtp3SentBytes_Type())
cItpActMtp3SentBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActMtp3SentBytes.setStatus(_A)
if mibBuilder.loadTexts:cItpActMtp3SentBytes.setUnits(_E)
_CItpActGtt_ObjectIdentity=ObjectIdentity
cItpActGtt=_CItpActGtt_ObjectIdentity((1,3,6,1,4,1,9,9,230,1,2))
_CItpActGttTable_Object=MibTable
cItpActGttTable=_CItpActGttTable_Object((1,3,6,1,4,1,9,9,230,1,2,1))
if mibBuilder.loadTexts:cItpActGttTable.setStatus(_A)
_CItpActGttTableEntry_Object=MibTableRow
cItpActGttTableEntry=_CItpActGttTableEntry_Object((1,3,6,1,4,1,9,9,230,1,2,1,1))
cItpActGttTableEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:cItpActGttTableEntry.setStatus(_A)
_CItpActGttLinksetName_Type=CItpTcLinksetId
_CItpActGttLinksetName_Object=MibTableColumn
cItpActGttLinksetName=_CItpActGttLinksetName_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,1),_CItpActGttLinksetName_Type())
cItpActGttLinksetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActGttLinksetName.setStatus(_A)
_CItpActGttSelectorName_Type=CItpTcGlobalTitleSelectorName
_CItpActGttSelectorName_Object=MibTableColumn
cItpActGttSelectorName=_CItpActGttSelectorName_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,2),_CItpActGttSelectorName_Type())
cItpActGttSelectorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActGttSelectorName.setStatus(_A)
_CItpActGttGta_Type=CItpTcGtaAddr
_CItpActGttGta_Object=MibTableColumn
cItpActGttGta=_CItpActGttGta_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,3),_CItpActGttGta_Type())
cItpActGttGta.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActGttGta.setStatus(_A)
_CItpActGttTranslatedPc_Type=CItpTcPointCode
_CItpActGttTranslatedPc_Object=MibTableColumn
cItpActGttTranslatedPc=_CItpActGttTranslatedPc_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,4),_CItpActGttTranslatedPc_Type())
cItpActGttTranslatedPc.setMaxAccess(_C)
if mibBuilder.loadTexts:cItpActGttTranslatedPc.setStatus(_A)
_CItpActGttPackets_Type=Counter32
_CItpActGttPackets_Object=MibTableColumn
cItpActGttPackets=_CItpActGttPackets_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,5),_CItpActGttPackets_Type())
cItpActGttPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActGttPackets.setStatus(_A)
if mibBuilder.loadTexts:cItpActGttPackets.setUnits(_E)
_CItpActGttBytes_Type=Counter32
_CItpActGttBytes_Object=MibTableColumn
cItpActGttBytes=_CItpActGttBytes_Object((1,3,6,1,4,1,9,9,230,1,2,1,1,6),_CItpActGttBytes_Type())
cItpActGttBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cItpActGttBytes.setStatus(_A)
if mibBuilder.loadTexts:cItpActGttBytes.setUnits(_E)
_CItpActMIBConformance_ObjectIdentity=ObjectIdentity
cItpActMIBConformance=_CItpActMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,230,2))
_CItpActMIBCompliances_ObjectIdentity=ObjectIdentity
cItpActMIBCompliances=_CItpActMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,230,2,1))
_CItpActMIBGroups_ObjectIdentity=ObjectIdentity
cItpActMIBGroups=_CItpActMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,230,2,2))
cItpActMtp3Group=ObjectGroup((1,3,6,1,4,1,9,9,230,2,2,1))
cItpActMtp3Group.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cItpActMtp3Group.setStatus(_A)
cItpActGttGroup=ObjectGroup((1,3,6,1,4,1,9,9,230,2,2,2))
cItpActGttGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cItpActGttGroup.setStatus(_A)
cItpActMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,230,2,1,1))
cItpActMIBCompliance.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cItpActMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoItpActMIB':ciscoItpActMIB,'cItpActMIBNotifs':cItpActMIBNotifs,'cItpActMIBObjects':cItpActMIBObjects,'cItpActMtp3':cItpActMtp3,'cItpActMtp3Table':cItpActMtp3Table,'cItpActMtp3TableEntry':cItpActMtp3TableEntry,_G:cItpActMtp3TableId,_H:cItpActMtp3LinksetName,_I:cItpActMtp3Dpc,_J:cItpActMtp3Opc,_K:cItpActMtp3SI,_Q:cItpActMtp3RcvdPackets,_R:cItpActMtp3SentPackets,_S:cItpActMtp3RcvdBytes,_T:cItpActMtp3SentBytes,'cItpActGtt':cItpActGtt,'cItpActGttTable':cItpActGttTable,'cItpActGttTableEntry':cItpActGttTableEntry,_M:cItpActGttLinksetName,_N:cItpActGttSelectorName,_O:cItpActGttGta,_P:cItpActGttTranslatedPc,_U:cItpActGttPackets,_V:cItpActGttBytes,'cItpActMIBConformance':cItpActMIBConformance,'cItpActMIBCompliances':cItpActMIBCompliances,'cItpActMIBCompliance':cItpActMIBCompliance,'cItpActMIBGroups':cItpActMIBGroups,_W:cItpActMtp3Group,_X:cItpActGttGroup})