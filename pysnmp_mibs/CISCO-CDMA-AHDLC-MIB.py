_l='cCdmaAhdlcNotifGroup'
_k='cCdmaAhdlcGroup'
_j='cCdmaAhdlcEngineDownNotif'
_i='cCdmaAhdlcDiscontinuityTime'
_h='cCdmaAhdlcInvSizeDropPktsEnc'
_g='cCdmaAhdlcInvSizeDropPktsDec'
_f='cCdmaAhdlcOverflowDropPktsEnc'
_e='cCdmaAhdlcOverflowDropPktsDec'
_d='cCdmaAhdlcMemDropPktsEnc'
_c='cCdmaAhdlcMemDropPktsDec'
_b='cCdmaAhdlcCRCDropPkts'
_a='cCdmaAhdlcDropPktsEnc'
_Z='cCdmaAhdlcDropPktsDec'
_Y='cCdmaAhdlcIncomingPktsDecoded'
_X='cCdmaAhdlcIncomingPktsToDecode'
_W='cCdmaAhdlcIncomingOctetsDecoded'
_V='cCdmaAhdlcIncomingOctetsToDecode'
_U='cCdmaAhdlcOutgoingPktsEncoded'
_T='cCdmaAhdlcOutgoingPktsToEncode'
_S='cCdmaAhdlcOutgoingOctetsEncoded'
_R='cCdmaAhdlcOutgoingOctetsToEncode'
_Q='cCdmaAhdlcPhysicalIndex'
_P='cCdmaAhdlcEngineDownNotifEnabled'
_O='cCdmaAhdlcEngineChannelsInUse'
_N='cCdmaAhdlcEngineConfMaxChannels'
_M='cCdmaAhdlcEngineMaxChannels'
_L='cCdmaAhdlcEngineType'
_K='cCdmaAhdlcEngineName'
_J='cCdmaAhdlcPerfEntry'
_I='unknown'
_H='cCdmaAhdlcEngineIndex'
_G='cCdmaAhdlcEngineAdminState'
_F='cCdmaAhdlcEngineOperState'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-CDMA-AHDLC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
cCdmaAhdlcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,997))
if mibBuilder.loadTexts:cCdmaAhdlcMIB.setRevisions(('2005-11-14 00:00','2002-01-04 00:00'))
_CCdmaAhdlcMIBNotif_ObjectIdentity=ObjectIdentity
cCdmaAhdlcMIBNotif=_CCdmaAhdlcMIBNotif_ObjectIdentity((1,3,6,1,4,1,9,9,997,0))
_CCdmaAhdlcMIBObjects_ObjectIdentity=ObjectIdentity
cCdmaAhdlcMIBObjects=_CCdmaAhdlcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,997,1))
_CCdmaAhdlcEngineInfo_ObjectIdentity=ObjectIdentity
cCdmaAhdlcEngineInfo=_CCdmaAhdlcEngineInfo_ObjectIdentity((1,3,6,1,4,1,9,9,997,1,1))
_CCdmaAhdlcEngineTable_Object=MibTable
cCdmaAhdlcEngineTable=_CCdmaAhdlcEngineTable_Object((1,3,6,1,4,1,9,9,997,1,1,1))
if mibBuilder.loadTexts:cCdmaAhdlcEngineTable.setStatus(_A)
_CCdmaAhdlcEngineEntry_Object=MibTableRow
cCdmaAhdlcEngineEntry=_CCdmaAhdlcEngineEntry_Object((1,3,6,1,4,1,9,9,997,1,1,1,1))
cCdmaAhdlcEngineEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cCdmaAhdlcEngineEntry.setStatus(_A)
_CCdmaAhdlcEngineIndex_Type=Unsigned32
_CCdmaAhdlcEngineIndex_Object=MibTableColumn
cCdmaAhdlcEngineIndex=_CCdmaAhdlcEngineIndex_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,1),_CCdmaAhdlcEngineIndex_Type())
cCdmaAhdlcEngineIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cCdmaAhdlcEngineIndex.setStatus(_A)
_CCdmaAhdlcEngineName_Type=SnmpAdminString
_CCdmaAhdlcEngineName_Object=MibTableColumn
cCdmaAhdlcEngineName=_CCdmaAhdlcEngineName_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,2),_CCdmaAhdlcEngineName_Type())
cCdmaAhdlcEngineName.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcEngineName.setStatus(_A)
class _CCdmaAhdlcEngineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('software',1),('hardware',2)))
_CCdmaAhdlcEngineType_Type.__name__=_D
_CCdmaAhdlcEngineType_Object=MibTableColumn
cCdmaAhdlcEngineType=_CCdmaAhdlcEngineType_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,3),_CCdmaAhdlcEngineType_Type())
cCdmaAhdlcEngineType.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcEngineType.setStatus(_A)
_CCdmaAhdlcEngineChannelsInUse_Type=Gauge32
_CCdmaAhdlcEngineChannelsInUse_Object=MibTableColumn
cCdmaAhdlcEngineChannelsInUse=_CCdmaAhdlcEngineChannelsInUse_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,4),_CCdmaAhdlcEngineChannelsInUse_Type())
cCdmaAhdlcEngineChannelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcEngineChannelsInUse.setStatus(_A)
_CCdmaAhdlcEngineMaxChannels_Type=Unsigned32
_CCdmaAhdlcEngineMaxChannels_Object=MibTableColumn
cCdmaAhdlcEngineMaxChannels=_CCdmaAhdlcEngineMaxChannels_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,5),_CCdmaAhdlcEngineMaxChannels_Type())
cCdmaAhdlcEngineMaxChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcEngineMaxChannels.setStatus(_A)
_CCdmaAhdlcEngineConfMaxChannels_Type=Unsigned32
_CCdmaAhdlcEngineConfMaxChannels_Object=MibTableColumn
cCdmaAhdlcEngineConfMaxChannels=_CCdmaAhdlcEngineConfMaxChannels_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,6),_CCdmaAhdlcEngineConfMaxChannels_Type())
cCdmaAhdlcEngineConfMaxChannels.setMaxAccess(_E)
if mibBuilder.loadTexts:cCdmaAhdlcEngineConfMaxChannels.setStatus(_A)
class _CCdmaAhdlcEngineOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('up',1),('down',2)))
_CCdmaAhdlcEngineOperState_Type.__name__=_D
_CCdmaAhdlcEngineOperState_Object=MibTableColumn
cCdmaAhdlcEngineOperState=_CCdmaAhdlcEngineOperState_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,7),_CCdmaAhdlcEngineOperState_Type())
cCdmaAhdlcEngineOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcEngineOperState.setStatus(_A)
class _CCdmaAhdlcEngineAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CCdmaAhdlcEngineAdminState_Type.__name__=_D
_CCdmaAhdlcEngineAdminState_Object=MibTableColumn
cCdmaAhdlcEngineAdminState=_CCdmaAhdlcEngineAdminState_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,8),_CCdmaAhdlcEngineAdminState_Type())
cCdmaAhdlcEngineAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:cCdmaAhdlcEngineAdminState.setStatus(_A)
_CCdmaAhdlcEngineDownNotifEnabled_Type=TruthValue
_CCdmaAhdlcEngineDownNotifEnabled_Object=MibTableColumn
cCdmaAhdlcEngineDownNotifEnabled=_CCdmaAhdlcEngineDownNotifEnabled_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,9),_CCdmaAhdlcEngineDownNotifEnabled_Type())
cCdmaAhdlcEngineDownNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cCdmaAhdlcEngineDownNotifEnabled.setStatus(_A)
_CCdmaAhdlcPhysicalIndex_Type=EntPhysicalIndexOrZero
_CCdmaAhdlcPhysicalIndex_Object=MibTableColumn
cCdmaAhdlcPhysicalIndex=_CCdmaAhdlcPhysicalIndex_Object((1,3,6,1,4,1,9,9,997,1,1,1,1,10),_CCdmaAhdlcPhysicalIndex_Type())
cCdmaAhdlcPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcPhysicalIndex.setStatus(_A)
_CCdmaAhdlcPerfTable_Object=MibTable
cCdmaAhdlcPerfTable=_CCdmaAhdlcPerfTable_Object((1,3,6,1,4,1,9,9,997,1,1,2))
if mibBuilder.loadTexts:cCdmaAhdlcPerfTable.setStatus(_A)
_CCdmaAhdlcPerfEntry_Object=MibTableRow
cCdmaAhdlcPerfEntry=_CCdmaAhdlcPerfEntry_Object((1,3,6,1,4,1,9,9,997,1,1,2,1))
if mibBuilder.loadTexts:cCdmaAhdlcPerfEntry.setStatus(_A)
_CCdmaAhdlcOutgoingOctetsToEncode_Type=ZeroBasedCounter32
_CCdmaAhdlcOutgoingOctetsToEncode_Object=MibTableColumn
cCdmaAhdlcOutgoingOctetsToEncode=_CCdmaAhdlcOutgoingOctetsToEncode_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,1),_CCdmaAhdlcOutgoingOctetsToEncode_Type())
cCdmaAhdlcOutgoingOctetsToEncode.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOutgoingOctetsToEncode.setStatus(_A)
_CCdmaAhdlcOutgoingOctetsEncoded_Type=ZeroBasedCounter32
_CCdmaAhdlcOutgoingOctetsEncoded_Object=MibTableColumn
cCdmaAhdlcOutgoingOctetsEncoded=_CCdmaAhdlcOutgoingOctetsEncoded_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,2),_CCdmaAhdlcOutgoingOctetsEncoded_Type())
cCdmaAhdlcOutgoingOctetsEncoded.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOutgoingOctetsEncoded.setStatus(_A)
_CCdmaAhdlcOutgoingPktsToEncode_Type=ZeroBasedCounter32
_CCdmaAhdlcOutgoingPktsToEncode_Object=MibTableColumn
cCdmaAhdlcOutgoingPktsToEncode=_CCdmaAhdlcOutgoingPktsToEncode_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,3),_CCdmaAhdlcOutgoingPktsToEncode_Type())
cCdmaAhdlcOutgoingPktsToEncode.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOutgoingPktsToEncode.setStatus(_A)
_CCdmaAhdlcOutgoingPktsEncoded_Type=ZeroBasedCounter32
_CCdmaAhdlcOutgoingPktsEncoded_Object=MibTableColumn
cCdmaAhdlcOutgoingPktsEncoded=_CCdmaAhdlcOutgoingPktsEncoded_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,4),_CCdmaAhdlcOutgoingPktsEncoded_Type())
cCdmaAhdlcOutgoingPktsEncoded.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOutgoingPktsEncoded.setStatus(_A)
_CCdmaAhdlcIncomingOctetsToDecode_Type=ZeroBasedCounter32
_CCdmaAhdlcIncomingOctetsToDecode_Object=MibTableColumn
cCdmaAhdlcIncomingOctetsToDecode=_CCdmaAhdlcIncomingOctetsToDecode_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,5),_CCdmaAhdlcIncomingOctetsToDecode_Type())
cCdmaAhdlcIncomingOctetsToDecode.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcIncomingOctetsToDecode.setStatus(_A)
_CCdmaAhdlcIncomingOctetsDecoded_Type=ZeroBasedCounter32
_CCdmaAhdlcIncomingOctetsDecoded_Object=MibTableColumn
cCdmaAhdlcIncomingOctetsDecoded=_CCdmaAhdlcIncomingOctetsDecoded_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,6),_CCdmaAhdlcIncomingOctetsDecoded_Type())
cCdmaAhdlcIncomingOctetsDecoded.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcIncomingOctetsDecoded.setStatus(_A)
_CCdmaAhdlcIncomingPktsToDecode_Type=ZeroBasedCounter32
_CCdmaAhdlcIncomingPktsToDecode_Object=MibTableColumn
cCdmaAhdlcIncomingPktsToDecode=_CCdmaAhdlcIncomingPktsToDecode_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,7),_CCdmaAhdlcIncomingPktsToDecode_Type())
cCdmaAhdlcIncomingPktsToDecode.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcIncomingPktsToDecode.setStatus(_A)
_CCdmaAhdlcIncomingPktsDecoded_Type=ZeroBasedCounter32
_CCdmaAhdlcIncomingPktsDecoded_Object=MibTableColumn
cCdmaAhdlcIncomingPktsDecoded=_CCdmaAhdlcIncomingPktsDecoded_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,8),_CCdmaAhdlcIncomingPktsDecoded_Type())
cCdmaAhdlcIncomingPktsDecoded.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcIncomingPktsDecoded.setStatus(_A)
_CCdmaAhdlcDropPktsDec_Type=ZeroBasedCounter32
_CCdmaAhdlcDropPktsDec_Object=MibTableColumn
cCdmaAhdlcDropPktsDec=_CCdmaAhdlcDropPktsDec_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,9),_CCdmaAhdlcDropPktsDec_Type())
cCdmaAhdlcDropPktsDec.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcDropPktsDec.setStatus(_A)
_CCdmaAhdlcDropPktsEnc_Type=ZeroBasedCounter32
_CCdmaAhdlcDropPktsEnc_Object=MibTableColumn
cCdmaAhdlcDropPktsEnc=_CCdmaAhdlcDropPktsEnc_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,10),_CCdmaAhdlcDropPktsEnc_Type())
cCdmaAhdlcDropPktsEnc.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcDropPktsEnc.setStatus(_A)
_CCdmaAhdlcCRCDropPkts_Type=ZeroBasedCounter32
_CCdmaAhdlcCRCDropPkts_Object=MibTableColumn
cCdmaAhdlcCRCDropPkts=_CCdmaAhdlcCRCDropPkts_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,11),_CCdmaAhdlcCRCDropPkts_Type())
cCdmaAhdlcCRCDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcCRCDropPkts.setStatus(_A)
_CCdmaAhdlcMemDropPktsDec_Type=ZeroBasedCounter32
_CCdmaAhdlcMemDropPktsDec_Object=MibTableColumn
cCdmaAhdlcMemDropPktsDec=_CCdmaAhdlcMemDropPktsDec_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,12),_CCdmaAhdlcMemDropPktsDec_Type())
cCdmaAhdlcMemDropPktsDec.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcMemDropPktsDec.setStatus(_A)
_CCdmaAhdlcMemDropPktsEnc_Type=ZeroBasedCounter32
_CCdmaAhdlcMemDropPktsEnc_Object=MibTableColumn
cCdmaAhdlcMemDropPktsEnc=_CCdmaAhdlcMemDropPktsEnc_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,13),_CCdmaAhdlcMemDropPktsEnc_Type())
cCdmaAhdlcMemDropPktsEnc.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcMemDropPktsEnc.setStatus(_A)
_CCdmaAhdlcOverflowDropPktsDec_Type=ZeroBasedCounter32
_CCdmaAhdlcOverflowDropPktsDec_Object=MibTableColumn
cCdmaAhdlcOverflowDropPktsDec=_CCdmaAhdlcOverflowDropPktsDec_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,14),_CCdmaAhdlcOverflowDropPktsDec_Type())
cCdmaAhdlcOverflowDropPktsDec.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOverflowDropPktsDec.setStatus(_A)
_CCdmaAhdlcOverflowDropPktsEnc_Type=ZeroBasedCounter32
_CCdmaAhdlcOverflowDropPktsEnc_Object=MibTableColumn
cCdmaAhdlcOverflowDropPktsEnc=_CCdmaAhdlcOverflowDropPktsEnc_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,15),_CCdmaAhdlcOverflowDropPktsEnc_Type())
cCdmaAhdlcOverflowDropPktsEnc.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcOverflowDropPktsEnc.setStatus(_A)
_CCdmaAhdlcInvSizeDropPktsDec_Type=ZeroBasedCounter32
_CCdmaAhdlcInvSizeDropPktsDec_Object=MibTableColumn
cCdmaAhdlcInvSizeDropPktsDec=_CCdmaAhdlcInvSizeDropPktsDec_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,16),_CCdmaAhdlcInvSizeDropPktsDec_Type())
cCdmaAhdlcInvSizeDropPktsDec.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcInvSizeDropPktsDec.setStatus(_A)
_CCdmaAhdlcInvSizeDropPktsEnc_Type=ZeroBasedCounter32
_CCdmaAhdlcInvSizeDropPktsEnc_Object=MibTableColumn
cCdmaAhdlcInvSizeDropPktsEnc=_CCdmaAhdlcInvSizeDropPktsEnc_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,17),_CCdmaAhdlcInvSizeDropPktsEnc_Type())
cCdmaAhdlcInvSizeDropPktsEnc.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcInvSizeDropPktsEnc.setStatus(_A)
_CCdmaAhdlcDiscontinuityTime_Type=TimeStamp
_CCdmaAhdlcDiscontinuityTime_Object=MibTableColumn
cCdmaAhdlcDiscontinuityTime=_CCdmaAhdlcDiscontinuityTime_Object((1,3,6,1,4,1,9,9,997,1,1,2,1,18),_CCdmaAhdlcDiscontinuityTime_Type())
cCdmaAhdlcDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cCdmaAhdlcDiscontinuityTime.setStatus(_A)
_CCdmaAhdlcMIBConformance_ObjectIdentity=ObjectIdentity
cCdmaAhdlcMIBConformance=_CCdmaAhdlcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,997,3))
_CCdmaAhdlcMIBCompliances_ObjectIdentity=ObjectIdentity
cCdmaAhdlcMIBCompliances=_CCdmaAhdlcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,997,3,1))
_CCdmaAhdlcMIBGroups_ObjectIdentity=ObjectIdentity
cCdmaAhdlcMIBGroups=_CCdmaAhdlcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,997,3,2))
cCdmaAhdlcEngineEntry.registerAugmentions((_B,_J))
cCdmaAhdlcPerfEntry.setIndexNames(*cCdmaAhdlcEngineEntry.getIndexNames())
cCdmaAhdlcGroup=ObjectGroup((1,3,6,1,4,1,9,9,997,3,2,1))
cCdmaAhdlcGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_F),(_B,_G),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cCdmaAhdlcGroup.setStatus(_A)
cCdmaAhdlcEngineDownNotif=NotificationType((1,3,6,1,4,1,9,9,997,0,1))
cCdmaAhdlcEngineDownNotif.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cCdmaAhdlcEngineDownNotif.setStatus(_A)
cCdmaAhdlcNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,997,3,2,2))
cCdmaAhdlcNotifGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:cCdmaAhdlcNotifGroup.setStatus(_A)
cCdmaAhdlcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,997,3,1,1))
cCdmaAhdlcMIBCompliance.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cCdmaAhdlcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cCdmaAhdlcMIB':cCdmaAhdlcMIB,'cCdmaAhdlcMIBNotif':cCdmaAhdlcMIBNotif,_j:cCdmaAhdlcEngineDownNotif,'cCdmaAhdlcMIBObjects':cCdmaAhdlcMIBObjects,'cCdmaAhdlcEngineInfo':cCdmaAhdlcEngineInfo,'cCdmaAhdlcEngineTable':cCdmaAhdlcEngineTable,'cCdmaAhdlcEngineEntry':cCdmaAhdlcEngineEntry,_H:cCdmaAhdlcEngineIndex,_K:cCdmaAhdlcEngineName,_L:cCdmaAhdlcEngineType,_O:cCdmaAhdlcEngineChannelsInUse,_M:cCdmaAhdlcEngineMaxChannels,_N:cCdmaAhdlcEngineConfMaxChannels,_F:cCdmaAhdlcEngineOperState,_G:cCdmaAhdlcEngineAdminState,_P:cCdmaAhdlcEngineDownNotifEnabled,_Q:cCdmaAhdlcPhysicalIndex,'cCdmaAhdlcPerfTable':cCdmaAhdlcPerfTable,_J:cCdmaAhdlcPerfEntry,_R:cCdmaAhdlcOutgoingOctetsToEncode,_S:cCdmaAhdlcOutgoingOctetsEncoded,_T:cCdmaAhdlcOutgoingPktsToEncode,_U:cCdmaAhdlcOutgoingPktsEncoded,_V:cCdmaAhdlcIncomingOctetsToDecode,_W:cCdmaAhdlcIncomingOctetsDecoded,_X:cCdmaAhdlcIncomingPktsToDecode,_Y:cCdmaAhdlcIncomingPktsDecoded,_Z:cCdmaAhdlcDropPktsDec,_a:cCdmaAhdlcDropPktsEnc,_b:cCdmaAhdlcCRCDropPkts,_c:cCdmaAhdlcMemDropPktsDec,_d:cCdmaAhdlcMemDropPktsEnc,_e:cCdmaAhdlcOverflowDropPktsDec,_f:cCdmaAhdlcOverflowDropPktsEnc,_g:cCdmaAhdlcInvSizeDropPktsDec,_h:cCdmaAhdlcInvSizeDropPktsEnc,_i:cCdmaAhdlcDiscontinuityTime,'cCdmaAhdlcMIBConformance':cCdmaAhdlcMIBConformance,'cCdmaAhdlcMIBCompliances':cCdmaAhdlcMIBCompliances,'cCdmaAhdlcMIBCompliance':cCdmaAhdlcMIBCompliance,'cCdmaAhdlcMIBGroups':cCdmaAhdlcMIBGroups,_k:cCdmaAhdlcGroup,_l:cCdmaAhdlcNotifGroup})