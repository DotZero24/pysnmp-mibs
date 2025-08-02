_I='mpNetPingID'
_H='mpNetWatchID'
_G='NotificationType'
_F='MP-NETWATCH-MIB'
_E='down'
_D='up'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_Datax_mib_ObjectIdentity=ObjectIdentity
datax_mib=_Datax_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3))
_Mmpf_mib_ObjectIdentity=ObjectIdentity
mmpf_mib=_Mmpf_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13))
_MpInterface_ObjectIdentity=ObjectIdentity
mpInterface=_MpInterface_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,103))
_MpNetwatch_ObjectIdentity=ObjectIdentity
mpNetwatch=_MpNetwatch_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,132))
_MpNetWatchTable_Object=MibTable
mpNetWatchTable=_MpNetWatchTable_Object((1,3,6,1,4,1,119,2,3,3,13,132,1))
if mibBuilder.loadTexts:mpNetWatchTable.setStatus(_A)
_MpNetWatchEntry_Object=MibTableRow
mpNetWatchEntry=_MpNetWatchEntry_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1))
mpNetWatchEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:mpNetWatchEntry.setStatus(_A)
_MpNetWatchID_Type=Integer32
_MpNetWatchID_Object=MibTableColumn
mpNetWatchID=_MpNetWatchID_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,1),_MpNetWatchID_Type())
mpNetWatchID.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchID.setStatus(_A)
_MpNetWatchVPNID_Type=Integer32
_MpNetWatchVPNID_Object=MibTableColumn
mpNetWatchVPNID=_MpNetWatchVPNID_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,2),_MpNetWatchVPNID_Type())
mpNetWatchVPNID.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchVPNID.setStatus(_A)
class _MpNetWatchEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('retry',3)))
_MpNetWatchEntryStatus_Type.__name__=_C
_MpNetWatchEntryStatus_Object=MibTableColumn
mpNetWatchEntryStatus=_MpNetWatchEntryStatus_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,3),_MpNetWatchEntryStatus_Type())
mpNetWatchEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchEntryStatus.setStatus(_A)
class _MpNetWatchAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_MpNetWatchAction_Type.__name__=_C
_MpNetWatchAction_Object=MibTableColumn
mpNetWatchAction=_MpNetWatchAction_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,4),_MpNetWatchAction_Type())
mpNetWatchAction.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchAction.setStatus(_A)
_MpNetWatchNetworkAddr1_Type=IpAddress
_MpNetWatchNetworkAddr1_Object=MibTableColumn
mpNetWatchNetworkAddr1=_MpNetWatchNetworkAddr1_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,5),_MpNetWatchNetworkAddr1_Type())
mpNetWatchNetworkAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr1.setStatus(_A)
_MpNetWatchSubNetMask1_Type=IpAddress
_MpNetWatchSubNetMask1_Object=MibTableColumn
mpNetWatchSubNetMask1=_MpNetWatchSubNetMask1_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,6),_MpNetWatchSubNetMask1_Type())
mpNetWatchSubNetMask1.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask1.setStatus(_A)
_MpNetWatchNetworkAddr2_Type=IpAddress
_MpNetWatchNetworkAddr2_Object=MibTableColumn
mpNetWatchNetworkAddr2=_MpNetWatchNetworkAddr2_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,7),_MpNetWatchNetworkAddr2_Type())
mpNetWatchNetworkAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr2.setStatus(_A)
_MpNetWatchSubNetMask2_Type=IpAddress
_MpNetWatchSubNetMask2_Object=MibTableColumn
mpNetWatchSubNetMask2=_MpNetWatchSubNetMask2_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,8),_MpNetWatchSubNetMask2_Type())
mpNetWatchSubNetMask2.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask2.setStatus(_A)
_MpNetWatchNetworkAddr3_Type=IpAddress
_MpNetWatchNetworkAddr3_Object=MibTableColumn
mpNetWatchNetworkAddr3=_MpNetWatchNetworkAddr3_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,9),_MpNetWatchNetworkAddr3_Type())
mpNetWatchNetworkAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr3.setStatus(_A)
_MpNetWatchSubNetMask3_Type=IpAddress
_MpNetWatchSubNetMask3_Object=MibTableColumn
mpNetWatchSubNetMask3=_MpNetWatchSubNetMask3_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,10),_MpNetWatchSubNetMask3_Type())
mpNetWatchSubNetMask3.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask3.setStatus(_A)
_MpNetWatchNetworkAddr4_Type=IpAddress
_MpNetWatchNetworkAddr4_Object=MibTableColumn
mpNetWatchNetworkAddr4=_MpNetWatchNetworkAddr4_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,11),_MpNetWatchNetworkAddr4_Type())
mpNetWatchNetworkAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr4.setStatus(_A)
_MpNetWatchSubNetMask4_Type=IpAddress
_MpNetWatchSubNetMask4_Object=MibTableColumn
mpNetWatchSubNetMask4=_MpNetWatchSubNetMask4_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,12),_MpNetWatchSubNetMask4_Type())
mpNetWatchSubNetMask4.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask4.setStatus(_A)
_MpNetWatchNetworkAddr5_Type=IpAddress
_MpNetWatchNetworkAddr5_Object=MibTableColumn
mpNetWatchNetworkAddr5=_MpNetWatchNetworkAddr5_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,13),_MpNetWatchNetworkAddr5_Type())
mpNetWatchNetworkAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr5.setStatus(_A)
_MpNetWatchSubNetMask5_Type=IpAddress
_MpNetWatchSubNetMask5_Object=MibTableColumn
mpNetWatchSubNetMask5=_MpNetWatchSubNetMask5_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,14),_MpNetWatchSubNetMask5_Type())
mpNetWatchSubNetMask5.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask5.setStatus(_A)
_MpNetWatchNetworkAddr6_Type=IpAddress
_MpNetWatchNetworkAddr6_Object=MibTableColumn
mpNetWatchNetworkAddr6=_MpNetWatchNetworkAddr6_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,15),_MpNetWatchNetworkAddr6_Type())
mpNetWatchNetworkAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr6.setStatus(_A)
_MpNetWatchSubNetMask6_Type=IpAddress
_MpNetWatchSubNetMask6_Object=MibTableColumn
mpNetWatchSubNetMask6=_MpNetWatchSubNetMask6_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,16),_MpNetWatchSubNetMask6_Type())
mpNetWatchSubNetMask6.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask6.setStatus(_A)
_MpNetWatchNetworkAddr7_Type=IpAddress
_MpNetWatchNetworkAddr7_Object=MibTableColumn
mpNetWatchNetworkAddr7=_MpNetWatchNetworkAddr7_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,17),_MpNetWatchNetworkAddr7_Type())
mpNetWatchNetworkAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr7.setStatus(_A)
_MpNetWatchSubNetMask7_Type=IpAddress
_MpNetWatchSubNetMask7_Object=MibTableColumn
mpNetWatchSubNetMask7=_MpNetWatchSubNetMask7_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,18),_MpNetWatchSubNetMask7_Type())
mpNetWatchSubNetMask7.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask7.setStatus(_A)
_MpNetWatchNetworkAddr8_Type=IpAddress
_MpNetWatchNetworkAddr8_Object=MibTableColumn
mpNetWatchNetworkAddr8=_MpNetWatchNetworkAddr8_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,19),_MpNetWatchNetworkAddr8_Type())
mpNetWatchNetworkAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchNetworkAddr8.setStatus(_A)
_MpNetWatchSubNetMask8_Type=IpAddress
_MpNetWatchSubNetMask8_Object=MibTableColumn
mpNetWatchSubNetMask8=_MpNetWatchSubNetMask8_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,20),_MpNetWatchSubNetMask8_Type())
mpNetWatchSubNetMask8.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchSubNetMask8.setStatus(_A)
_MpNetWatchifIndex1_Type=Integer32
_MpNetWatchifIndex1_Object=MibTableColumn
mpNetWatchifIndex1=_MpNetWatchifIndex1_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,21),_MpNetWatchifIndex1_Type())
mpNetWatchifIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex1.setStatus(_A)
_MpNetWatchifIndex2_Type=Integer32
_MpNetWatchifIndex2_Object=MibTableColumn
mpNetWatchifIndex2=_MpNetWatchifIndex2_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,22),_MpNetWatchifIndex2_Type())
mpNetWatchifIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex2.setStatus(_A)
_MpNetWatchifIndex3_Type=Integer32
_MpNetWatchifIndex3_Object=MibTableColumn
mpNetWatchifIndex3=_MpNetWatchifIndex3_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,23),_MpNetWatchifIndex3_Type())
mpNetWatchifIndex3.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex3.setStatus(_A)
_MpNetWatchifIndex4_Type=Integer32
_MpNetWatchifIndex4_Object=MibTableColumn
mpNetWatchifIndex4=_MpNetWatchifIndex4_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,24),_MpNetWatchifIndex4_Type())
mpNetWatchifIndex4.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex4.setStatus(_A)
_MpNetWatchifIndex5_Type=Integer32
_MpNetWatchifIndex5_Object=MibTableColumn
mpNetWatchifIndex5=_MpNetWatchifIndex5_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,25),_MpNetWatchifIndex5_Type())
mpNetWatchifIndex5.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex5.setStatus(_A)
_MpNetWatchifIndex6_Type=Integer32
_MpNetWatchifIndex6_Object=MibTableColumn
mpNetWatchifIndex6=_MpNetWatchifIndex6_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,26),_MpNetWatchifIndex6_Type())
mpNetWatchifIndex6.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex6.setStatus(_A)
_MpNetWatchifIndex7_Type=Integer32
_MpNetWatchifIndex7_Object=MibTableColumn
mpNetWatchifIndex7=_MpNetWatchifIndex7_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,27),_MpNetWatchifIndex7_Type())
mpNetWatchifIndex7.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex7.setStatus(_A)
_MpNetWatchifIndex8_Type=Integer32
_MpNetWatchifIndex8_Object=MibTableColumn
mpNetWatchifIndex8=_MpNetWatchifIndex8_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,28),_MpNetWatchifIndex8_Type())
mpNetWatchifIndex8.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex8.setStatus(_A)
_MpNetWatchifIndex9_Type=Integer32
_MpNetWatchifIndex9_Object=MibTableColumn
mpNetWatchifIndex9=_MpNetWatchifIndex9_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,29),_MpNetWatchifIndex9_Type())
mpNetWatchifIndex9.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex9.setStatus(_A)
_MpNetWatchifIndex10_Type=Integer32
_MpNetWatchifIndex10_Object=MibTableColumn
mpNetWatchifIndex10=_MpNetWatchifIndex10_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,30),_MpNetWatchifIndex10_Type())
mpNetWatchifIndex10.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex10.setStatus(_A)
_MpNetWatchifIndex11_Type=Integer32
_MpNetWatchifIndex11_Object=MibTableColumn
mpNetWatchifIndex11=_MpNetWatchifIndex11_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,31),_MpNetWatchifIndex11_Type())
mpNetWatchifIndex11.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex11.setStatus(_A)
_MpNetWatchifIndex12_Type=Integer32
_MpNetWatchifIndex12_Object=MibTableColumn
mpNetWatchifIndex12=_MpNetWatchifIndex12_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,32),_MpNetWatchifIndex12_Type())
mpNetWatchifIndex12.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex12.setStatus(_A)
_MpNetWatchifIndex13_Type=Integer32
_MpNetWatchifIndex13_Object=MibTableColumn
mpNetWatchifIndex13=_MpNetWatchifIndex13_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,33),_MpNetWatchifIndex13_Type())
mpNetWatchifIndex13.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex13.setStatus(_A)
_MpNetWatchifIndex14_Type=Integer32
_MpNetWatchifIndex14_Object=MibTableColumn
mpNetWatchifIndex14=_MpNetWatchifIndex14_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,34),_MpNetWatchifIndex14_Type())
mpNetWatchifIndex14.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex14.setStatus(_A)
_MpNetWatchifIndex15_Type=Integer32
_MpNetWatchifIndex15_Object=MibTableColumn
mpNetWatchifIndex15=_MpNetWatchifIndex15_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,35),_MpNetWatchifIndex15_Type())
mpNetWatchifIndex15.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex15.setStatus(_A)
_MpNetWatchifIndex16_Type=Integer32
_MpNetWatchifIndex16_Object=MibTableColumn
mpNetWatchifIndex16=_MpNetWatchifIndex16_Object((1,3,6,1,4,1,119,2,3,3,13,132,1,1,36),_MpNetWatchifIndex16_Type())
mpNetWatchifIndex16.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchifIndex16.setStatus(_A)
_MpNetWatchStatusTimeStamp_ObjectIdentity=ObjectIdentity
mpNetWatchStatusTimeStamp=_MpNetWatchStatusTimeStamp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,132,2))
_MpNetWatchStatusLastChange_Type=TimeTicks
_MpNetWatchStatusLastChange_Object=MibScalar
mpNetWatchStatusLastChange=_MpNetWatchStatusLastChange_Object((1,3,6,1,4,1,119,2,3,3,13,132,2,1),_MpNetWatchStatusLastChange_Type())
mpNetWatchStatusLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetWatchStatusLastChange.setStatus(_A)
_MpNetping_ObjectIdentity=ObjectIdentity
mpNetping=_MpNetping_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,133))
_MpNetPingTable_Object=MibTable
mpNetPingTable=_MpNetPingTable_Object((1,3,6,1,4,1,119,2,3,3,13,133,1))
if mibBuilder.loadTexts:mpNetPingTable.setStatus(_A)
_MpNetPingEntry_Object=MibTableRow
mpNetPingEntry=_MpNetPingEntry_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1))
mpNetPingEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:mpNetPingEntry.setStatus(_A)
_MpNetPingID_Type=Integer32
_MpNetPingID_Object=MibTableColumn
mpNetPingID=_MpNetPingID_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,1),_MpNetPingID_Type())
mpNetPingID.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingID.setStatus(_A)
_MpNetPingVPNID_Type=Integer32
_MpNetPingVPNID_Object=MibTableColumn
mpNetPingVPNID=_MpNetPingVPNID_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,2),_MpNetPingVPNID_Type())
mpNetPingVPNID.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingVPNID.setStatus(_A)
class _MpNetPingEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('retry',3)))
_MpNetPingEntryStatus_Type.__name__=_C
_MpNetPingEntryStatus_Object=MibTableColumn
mpNetPingEntryStatus=_MpNetPingEntryStatus_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,3),_MpNetPingEntryStatus_Type())
mpNetPingEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingEntryStatus.setStatus(_A)
class _MpNetPingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_MpNetPingAction_Type.__name__=_C
_MpNetPingAction_Object=MibTableColumn
mpNetPingAction=_MpNetPingAction_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,4),_MpNetPingAction_Type())
mpNetPingAction.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingAction.setStatus(_A)
_MpNetPingDestIPAddr1_Type=IpAddress
_MpNetPingDestIPAddr1_Object=MibTableColumn
mpNetPingDestIPAddr1=_MpNetPingDestIPAddr1_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,5),_MpNetPingDestIPAddr1_Type())
mpNetPingDestIPAddr1.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr1.setStatus(_A)
_MpNetPingDestIPAddr2_Type=IpAddress
_MpNetPingDestIPAddr2_Object=MibTableColumn
mpNetPingDestIPAddr2=_MpNetPingDestIPAddr2_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,6),_MpNetPingDestIPAddr2_Type())
mpNetPingDestIPAddr2.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr2.setStatus(_A)
_MpNetPingDestIPAddr3_Type=IpAddress
_MpNetPingDestIPAddr3_Object=MibTableColumn
mpNetPingDestIPAddr3=_MpNetPingDestIPAddr3_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,7),_MpNetPingDestIPAddr3_Type())
mpNetPingDestIPAddr3.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr3.setStatus(_A)
_MpNetPingDestIPAddr4_Type=IpAddress
_MpNetPingDestIPAddr4_Object=MibTableColumn
mpNetPingDestIPAddr4=_MpNetPingDestIPAddr4_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,8),_MpNetPingDestIPAddr4_Type())
mpNetPingDestIPAddr4.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr4.setStatus(_A)
_MpNetPingDestIPAddr5_Type=IpAddress
_MpNetPingDestIPAddr5_Object=MibTableColumn
mpNetPingDestIPAddr5=_MpNetPingDestIPAddr5_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,9),_MpNetPingDestIPAddr5_Type())
mpNetPingDestIPAddr5.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr5.setStatus(_A)
_MpNetPingDestIPAddr6_Type=IpAddress
_MpNetPingDestIPAddr6_Object=MibTableColumn
mpNetPingDestIPAddr6=_MpNetPingDestIPAddr6_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,10),_MpNetPingDestIPAddr6_Type())
mpNetPingDestIPAddr6.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr6.setStatus(_A)
_MpNetPingDestIPAddr7_Type=IpAddress
_MpNetPingDestIPAddr7_Object=MibTableColumn
mpNetPingDestIPAddr7=_MpNetPingDestIPAddr7_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,11),_MpNetPingDestIPAddr7_Type())
mpNetPingDestIPAddr7.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr7.setStatus(_A)
_MpNetPingDestIPAddr8_Type=IpAddress
_MpNetPingDestIPAddr8_Object=MibTableColumn
mpNetPingDestIPAddr8=_MpNetPingDestIPAddr8_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,12),_MpNetPingDestIPAddr8_Type())
mpNetPingDestIPAddr8.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingDestIPAddr8.setStatus(_A)
_MpNetPingifIndex1_Type=Integer32
_MpNetPingifIndex1_Object=MibTableColumn
mpNetPingifIndex1=_MpNetPingifIndex1_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,13),_MpNetPingifIndex1_Type())
mpNetPingifIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex1.setStatus(_A)
_MpNetPingifIndex2_Type=Integer32
_MpNetPingifIndex2_Object=MibTableColumn
mpNetPingifIndex2=_MpNetPingifIndex2_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,14),_MpNetPingifIndex2_Type())
mpNetPingifIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex2.setStatus(_A)
_MpNetPingifIndex3_Type=Integer32
_MpNetPingifIndex3_Object=MibTableColumn
mpNetPingifIndex3=_MpNetPingifIndex3_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,15),_MpNetPingifIndex3_Type())
mpNetPingifIndex3.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex3.setStatus(_A)
_MpNetPingifIndex4_Type=Integer32
_MpNetPingifIndex4_Object=MibTableColumn
mpNetPingifIndex4=_MpNetPingifIndex4_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,16),_MpNetPingifIndex4_Type())
mpNetPingifIndex4.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex4.setStatus(_A)
_MpNetPingifIndex5_Type=Integer32
_MpNetPingifIndex5_Object=MibTableColumn
mpNetPingifIndex5=_MpNetPingifIndex5_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,17),_MpNetPingifIndex5_Type())
mpNetPingifIndex5.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex5.setStatus(_A)
_MpNetPingifIndex6_Type=Integer32
_MpNetPingifIndex6_Object=MibTableColumn
mpNetPingifIndex6=_MpNetPingifIndex6_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,18),_MpNetPingifIndex6_Type())
mpNetPingifIndex6.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex6.setStatus(_A)
_MpNetPingifIndex7_Type=Integer32
_MpNetPingifIndex7_Object=MibTableColumn
mpNetPingifIndex7=_MpNetPingifIndex7_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,19),_MpNetPingifIndex7_Type())
mpNetPingifIndex7.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex7.setStatus(_A)
_MpNetPingifIndex8_Type=Integer32
_MpNetPingifIndex8_Object=MibTableColumn
mpNetPingifIndex8=_MpNetPingifIndex8_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,20),_MpNetPingifIndex8_Type())
mpNetPingifIndex8.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex8.setStatus(_A)
_MpNetPingifIndex9_Type=Integer32
_MpNetPingifIndex9_Object=MibTableColumn
mpNetPingifIndex9=_MpNetPingifIndex9_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,21),_MpNetPingifIndex9_Type())
mpNetPingifIndex9.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex9.setStatus(_A)
_MpNetPingifIndex10_Type=Integer32
_MpNetPingifIndex10_Object=MibTableColumn
mpNetPingifIndex10=_MpNetPingifIndex10_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,22),_MpNetPingifIndex10_Type())
mpNetPingifIndex10.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex10.setStatus(_A)
_MpNetPingifIndex11_Type=Integer32
_MpNetPingifIndex11_Object=MibTableColumn
mpNetPingifIndex11=_MpNetPingifIndex11_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,23),_MpNetPingifIndex11_Type())
mpNetPingifIndex11.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex11.setStatus(_A)
_MpNetPingifIndex12_Type=Integer32
_MpNetPingifIndex12_Object=MibTableColumn
mpNetPingifIndex12=_MpNetPingifIndex12_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,24),_MpNetPingifIndex12_Type())
mpNetPingifIndex12.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex12.setStatus(_A)
_MpNetPingifIndex13_Type=Integer32
_MpNetPingifIndex13_Object=MibTableColumn
mpNetPingifIndex13=_MpNetPingifIndex13_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,25),_MpNetPingifIndex13_Type())
mpNetPingifIndex13.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex13.setStatus(_A)
_MpNetPingifIndex14_Type=Integer32
_MpNetPingifIndex14_Object=MibTableColumn
mpNetPingifIndex14=_MpNetPingifIndex14_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,26),_MpNetPingifIndex14_Type())
mpNetPingifIndex14.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex14.setStatus(_A)
_MpNetPingifIndex15_Type=Integer32
_MpNetPingifIndex15_Object=MibTableColumn
mpNetPingifIndex15=_MpNetPingifIndex15_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,27),_MpNetPingifIndex15_Type())
mpNetPingifIndex15.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex15.setStatus(_A)
_MpNetPingifIndex16_Type=Integer32
_MpNetPingifIndex16_Object=MibTableColumn
mpNetPingifIndex16=_MpNetPingifIndex16_Object((1,3,6,1,4,1,119,2,3,3,13,133,1,1,28),_MpNetPingifIndex16_Type())
mpNetPingifIndex16.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingifIndex16.setStatus(_A)
_MpNetPingStatusTimeStamp_ObjectIdentity=ObjectIdentity
mpNetPingStatusTimeStamp=_MpNetPingStatusTimeStamp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,133,2))
_MpNetPingStatusLastChange_Type=TimeTicks
_MpNetPingStatusLastChange_Object=MibScalar
mpNetPingStatusLastChange=_MpNetPingStatusLastChange_Object((1,3,6,1,4,1,119,2,3,3,13,133,2,1),_MpNetPingStatusLastChange_Type())
mpNetPingStatusLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:mpNetPingStatusLastChange.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'datax-mib':datax_mib,'mmpf-mib':mmpf_mib,'mpInterface':mpInterface,'mpNetwatch':mpNetwatch,'mpNetWatchTable':mpNetWatchTable,'mpNetWatchEntry':mpNetWatchEntry,_H:mpNetWatchID,'mpNetWatchVPNID':mpNetWatchVPNID,'mpNetWatchEntryStatus':mpNetWatchEntryStatus,'mpNetWatchAction':mpNetWatchAction,'mpNetWatchNetworkAddr1':mpNetWatchNetworkAddr1,'mpNetWatchSubNetMask1':mpNetWatchSubNetMask1,'mpNetWatchNetworkAddr2':mpNetWatchNetworkAddr2,'mpNetWatchSubNetMask2':mpNetWatchSubNetMask2,'mpNetWatchNetworkAddr3':mpNetWatchNetworkAddr3,'mpNetWatchSubNetMask3':mpNetWatchSubNetMask3,'mpNetWatchNetworkAddr4':mpNetWatchNetworkAddr4,'mpNetWatchSubNetMask4':mpNetWatchSubNetMask4,'mpNetWatchNetworkAddr5':mpNetWatchNetworkAddr5,'mpNetWatchSubNetMask5':mpNetWatchSubNetMask5,'mpNetWatchNetworkAddr6':mpNetWatchNetworkAddr6,'mpNetWatchSubNetMask6':mpNetWatchSubNetMask6,'mpNetWatchNetworkAddr7':mpNetWatchNetworkAddr7,'mpNetWatchSubNetMask7':mpNetWatchSubNetMask7,'mpNetWatchNetworkAddr8':mpNetWatchNetworkAddr8,'mpNetWatchSubNetMask8':mpNetWatchSubNetMask8,'mpNetWatchifIndex1':mpNetWatchifIndex1,'mpNetWatchifIndex2':mpNetWatchifIndex2,'mpNetWatchifIndex3':mpNetWatchifIndex3,'mpNetWatchifIndex4':mpNetWatchifIndex4,'mpNetWatchifIndex5':mpNetWatchifIndex5,'mpNetWatchifIndex6':mpNetWatchifIndex6,'mpNetWatchifIndex7':mpNetWatchifIndex7,'mpNetWatchifIndex8':mpNetWatchifIndex8,'mpNetWatchifIndex9':mpNetWatchifIndex9,'mpNetWatchifIndex10':mpNetWatchifIndex10,'mpNetWatchifIndex11':mpNetWatchifIndex11,'mpNetWatchifIndex12':mpNetWatchifIndex12,'mpNetWatchifIndex13':mpNetWatchifIndex13,'mpNetWatchifIndex14':mpNetWatchifIndex14,'mpNetWatchifIndex15':mpNetWatchifIndex15,'mpNetWatchifIndex16':mpNetWatchifIndex16,'mpNetWatchStatusTimeStamp':mpNetWatchStatusTimeStamp,'mpNetWatchStatusLastChange':mpNetWatchStatusLastChange,'mpNetping':mpNetping,'mpNetPingTable':mpNetPingTable,'mpNetPingEntry':mpNetPingEntry,_I:mpNetPingID,'mpNetPingVPNID':mpNetPingVPNID,'mpNetPingEntryStatus':mpNetPingEntryStatus,'mpNetPingAction':mpNetPingAction,'mpNetPingDestIPAddr1':mpNetPingDestIPAddr1,'mpNetPingDestIPAddr2':mpNetPingDestIPAddr2,'mpNetPingDestIPAddr3':mpNetPingDestIPAddr3,'mpNetPingDestIPAddr4':mpNetPingDestIPAddr4,'mpNetPingDestIPAddr5':mpNetPingDestIPAddr5,'mpNetPingDestIPAddr6':mpNetPingDestIPAddr6,'mpNetPingDestIPAddr7':mpNetPingDestIPAddr7,'mpNetPingDestIPAddr8':mpNetPingDestIPAddr8,'mpNetPingifIndex1':mpNetPingifIndex1,'mpNetPingifIndex2':mpNetPingifIndex2,'mpNetPingifIndex3':mpNetPingifIndex3,'mpNetPingifIndex4':mpNetPingifIndex4,'mpNetPingifIndex5':mpNetPingifIndex5,'mpNetPingifIndex6':mpNetPingifIndex6,'mpNetPingifIndex7':mpNetPingifIndex7,'mpNetPingifIndex8':mpNetPingifIndex8,'mpNetPingifIndex9':mpNetPingifIndex9,'mpNetPingifIndex10':mpNetPingifIndex10,'mpNetPingifIndex11':mpNetPingifIndex11,'mpNetPingifIndex12':mpNetPingifIndex12,'mpNetPingifIndex13':mpNetPingifIndex13,'mpNetPingifIndex14':mpNetPingifIndex14,'mpNetPingifIndex15':mpNetPingifIndex15,'mpNetPingifIndex16':mpNetPingifIndex16,'mpNetPingStatusTimeStamp':mpNetPingStatusTimeStamp,'mpNetPingStatusLastChange':mpNetPingStatusLastChange})