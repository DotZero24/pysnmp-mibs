_o='cwbIlmiStatsGroup'
_n='cwbIlmiConfGroup'
_m='bbIfSigCntClrButton'
_l='bbIfTooBigError'
_k='bbIfNoSuchNameError'
_j='bbIfAsn1ParseError'
_i='bbIfInvalidPDUReceived'
_h='bbIfTrapTransmitted'
_g='bbIfGetRequestTransmitted'
_f='bbIfGetResponseTransmitted'
_e='bbIfGetResponseReceived'
_d='bbIfTrapReceived'
_c='bbIfSetRequestReceived'
_b='bbIfGetNextRequestReceived'
_a='bbIfGetRequestReceived'
_Z='bbIfSnmpPduReceived'
_Y='bbIfAddrRegEnable'
_X='bbIfMinEnquiryIntervalT493'
_W='bbIfPollingIntervalT491'
_V='bbIfEventThresholdN492'
_U='bbIfErrorThresholdN491'
_T='bbIfKeepAlivePollingEnable'
_S='bbIfMinTrapInterval'
_R='bbIfIlmiTrapEnable'
_Q='bbIfProtocolRevNo'
_P='bbIfCustomerId'
_O='bbIfAddrPrefix'
_N='bbIfSignallingVci'
_M='bbIfSignallingVpi'
_L='bbIfSignallingProtocolType'
_K='bbIfIlmiEnable'
_J='seconds'
_I='sigCntBbIfNum'
_H='bbIfSigPortNum'
_G='enable'
_F='disable'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-BBIF-ILMI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmIlmiNetworkPrefix,=mibBuilder.importSymbols('ATM-TC-MIB','AtmIlmiNetworkPrefix')
bbIfCnf,bbIfCnt=mibBuilder.importSymbols('BASIS-MIB','bbIfCnf','bbIfCnt')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanBbifIlmiMIB=ModuleIdentity((1,3,6,1,4,1,351,150,33))
if mibBuilder.loadTexts:ciscoWanBbifIlmiMIB.setRevisions(('2002-12-20 00:00',))
_BbIfCnfSigILMIGrp_ObjectIdentity=ObjectIdentity
bbIfCnfSigILMIGrp=_BbIfCnfSigILMIGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,6,1,2))
_BbIfCnfSigILMIGrpTable_Object=MibTable
bbIfCnfSigILMIGrpTable=_BbIfCnfSigILMIGrpTable_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1))
if mibBuilder.loadTexts:bbIfCnfSigILMIGrpTable.setStatus(_A)
_BbIfCnfSigILMIGrpEntry_Object=MibTableRow
bbIfCnfSigILMIGrpEntry=_BbIfCnfSigILMIGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1))
bbIfCnfSigILMIGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:bbIfCnfSigILMIGrpEntry.setStatus(_A)
class _BbIfSigPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BbIfSigPortNum_Type.__name__=_C
_BbIfSigPortNum_Object=MibTableColumn
bbIfSigPortNum=_BbIfSigPortNum_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,1),_BbIfSigPortNum_Type())
bbIfSigPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfSigPortNum.setStatus(_A)
class _BbIfIlmiEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BbIfIlmiEnable_Type.__name__=_C
_BbIfIlmiEnable_Object=MibTableColumn
bbIfIlmiEnable=_BbIfIlmiEnable_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,2),_BbIfIlmiEnable_Type())
bbIfIlmiEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfIlmiEnable.setStatus(_A)
class _BbIfSignallingProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('noSignalling',2),('iLMI',3)))
_BbIfSignallingProtocolType_Type.__name__=_C
_BbIfSignallingProtocolType_Object=MibTableColumn
bbIfSignallingProtocolType=_BbIfSignallingProtocolType_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,3),_BbIfSignallingProtocolType_Type())
bbIfSignallingProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfSignallingProtocolType.setStatus(_A)
class _BbIfSignallingVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbIfSignallingVpi_Type.__name__=_C
_BbIfSignallingVpi_Object=MibTableColumn
bbIfSignallingVpi=_BbIfSignallingVpi_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,4),_BbIfSignallingVpi_Type())
bbIfSignallingVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfSignallingVpi.setStatus(_A)
class _BbIfSignallingVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BbIfSignallingVci_Type.__name__=_C
_BbIfSignallingVci_Object=MibTableColumn
bbIfSignallingVci=_BbIfSignallingVci_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,5),_BbIfSignallingVci_Type())
bbIfSignallingVci.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfSignallingVci.setStatus(_A)
_BbIfAddrPrefix_Type=AtmIlmiNetworkPrefix
_BbIfAddrPrefix_Object=MibTableColumn
bbIfAddrPrefix=_BbIfAddrPrefix_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,6),_BbIfAddrPrefix_Type())
bbIfAddrPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfAddrPrefix.setStatus(_A)
_BbIfCustomerId_Type=Integer32
_BbIfCustomerId_Object=MibTableColumn
bbIfCustomerId=_BbIfCustomerId_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,7),_BbIfCustomerId_Type())
bbIfCustomerId.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfCustomerId.setStatus(_A)
_BbIfProtocolRevNo_Type=Integer32
_BbIfProtocolRevNo_Object=MibTableColumn
bbIfProtocolRevNo=_BbIfProtocolRevNo_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,8),_BbIfProtocolRevNo_Type())
bbIfProtocolRevNo.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfProtocolRevNo.setStatus(_A)
class _BbIfIlmiTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BbIfIlmiTrapEnable_Type.__name__=_C
_BbIfIlmiTrapEnable_Object=MibTableColumn
bbIfIlmiTrapEnable=_BbIfIlmiTrapEnable_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,9),_BbIfIlmiTrapEnable_Type())
bbIfIlmiTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfIlmiTrapEnable.setStatus(_A)
class _BbIfMinTrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BbIfMinTrapInterval_Type.__name__=_C
_BbIfMinTrapInterval_Object=MibTableColumn
bbIfMinTrapInterval=_BbIfMinTrapInterval_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,10),_BbIfMinTrapInterval_Type())
bbIfMinTrapInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfMinTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:bbIfMinTrapInterval.setUnits(_J)
class _BbIfKeepAlivePollingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BbIfKeepAlivePollingEnable_Type.__name__=_C
_BbIfKeepAlivePollingEnable_Object=MibTableColumn
bbIfKeepAlivePollingEnable=_BbIfKeepAlivePollingEnable_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,11),_BbIfKeepAlivePollingEnable_Type())
bbIfKeepAlivePollingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfKeepAlivePollingEnable.setStatus(_A)
class _BbIfErrorThresholdN491_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BbIfErrorThresholdN491_Type.__name__=_C
_BbIfErrorThresholdN491_Object=MibTableColumn
bbIfErrorThresholdN491=_BbIfErrorThresholdN491_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,12),_BbIfErrorThresholdN491_Type())
bbIfErrorThresholdN491.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfErrorThresholdN491.setStatus(_A)
class _BbIfEventThresholdN492_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BbIfEventThresholdN492_Type.__name__=_C
_BbIfEventThresholdN492_Object=MibTableColumn
bbIfEventThresholdN492=_BbIfEventThresholdN492_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,13),_BbIfEventThresholdN492_Type())
bbIfEventThresholdN492.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfEventThresholdN492.setStatus(_A)
class _BbIfPollingIntervalT491_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,25,30,35,40,45,50,55,60)));namedValues=NamedValues(*(('v1',5),('v2',10),('v3',15),('v4',20),('v5',25),('v6',30),('v7',35),('v8',40),('v9',45),('v10',50),('v11',55),('v12',60)))
_BbIfPollingIntervalT491_Type.__name__=_C
_BbIfPollingIntervalT491_Object=MibTableColumn
bbIfPollingIntervalT491=_BbIfPollingIntervalT491_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,14),_BbIfPollingIntervalT491_Type())
bbIfPollingIntervalT491.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfPollingIntervalT491.setStatus(_A)
if mibBuilder.loadTexts:bbIfPollingIntervalT491.setUnits(_J)
class _BbIfMinEnquiryIntervalT493_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_BbIfMinEnquiryIntervalT493_Type.__name__=_C
_BbIfMinEnquiryIntervalT493_Object=MibTableColumn
bbIfMinEnquiryIntervalT493=_BbIfMinEnquiryIntervalT493_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,15),_BbIfMinEnquiryIntervalT493_Type())
bbIfMinEnquiryIntervalT493.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfMinEnquiryIntervalT493.setStatus(_A)
class _BbIfAddrRegEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BbIfAddrRegEnable_Type.__name__=_C
_BbIfAddrRegEnable_Object=MibTableColumn
bbIfAddrRegEnable=_BbIfAddrRegEnable_Object((1,3,6,1,4,1,351,110,5,2,6,1,2,1,1,16),_BbIfAddrRegEnable_Type())
bbIfAddrRegEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfAddrRegEnable.setStatus(_A)
_BbIfCntSigILMIGrp_ObjectIdentity=ObjectIdentity
bbIfCntSigILMIGrp=_BbIfCntSigILMIGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,6,4,2))
_BbIfCntSigILMIGrpTable_Object=MibTable
bbIfCntSigILMIGrpTable=_BbIfCntSigILMIGrpTable_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1))
if mibBuilder.loadTexts:bbIfCntSigILMIGrpTable.setStatus(_A)
_BbIfCntSigILMIGrpEntry_Object=MibTableRow
bbIfCntSigILMIGrpEntry=_BbIfCntSigILMIGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1))
bbIfCntSigILMIGrpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:bbIfCntSigILMIGrpEntry.setStatus(_A)
class _SigCntBbIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SigCntBbIfNum_Type.__name__=_C
_SigCntBbIfNum_Object=MibTableColumn
sigCntBbIfNum=_SigCntBbIfNum_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,1),_SigCntBbIfNum_Type())
sigCntBbIfNum.setMaxAccess(_E)
if mibBuilder.loadTexts:sigCntBbIfNum.setStatus(_A)
_BbIfSnmpPduReceived_Type=Counter32
_BbIfSnmpPduReceived_Object=MibTableColumn
bbIfSnmpPduReceived=_BbIfSnmpPduReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,2),_BbIfSnmpPduReceived_Type())
bbIfSnmpPduReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfSnmpPduReceived.setStatus(_A)
_BbIfGetRequestReceived_Type=Counter32
_BbIfGetRequestReceived_Object=MibTableColumn
bbIfGetRequestReceived=_BbIfGetRequestReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,3),_BbIfGetRequestReceived_Type())
bbIfGetRequestReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfGetRequestReceived.setStatus(_A)
_BbIfGetNextRequestReceived_Type=Counter32
_BbIfGetNextRequestReceived_Object=MibTableColumn
bbIfGetNextRequestReceived=_BbIfGetNextRequestReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,4),_BbIfGetNextRequestReceived_Type())
bbIfGetNextRequestReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfGetNextRequestReceived.setStatus(_A)
_BbIfSetRequestReceived_Type=Counter32
_BbIfSetRequestReceived_Object=MibTableColumn
bbIfSetRequestReceived=_BbIfSetRequestReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,5),_BbIfSetRequestReceived_Type())
bbIfSetRequestReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfSetRequestReceived.setStatus(_A)
_BbIfTrapReceived_Type=Counter32
_BbIfTrapReceived_Object=MibTableColumn
bbIfTrapReceived=_BbIfTrapReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,6),_BbIfTrapReceived_Type())
bbIfTrapReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfTrapReceived.setStatus(_A)
_BbIfGetResponseReceived_Type=Counter32
_BbIfGetResponseReceived_Object=MibTableColumn
bbIfGetResponseReceived=_BbIfGetResponseReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,7),_BbIfGetResponseReceived_Type())
bbIfGetResponseReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfGetResponseReceived.setStatus(_A)
_BbIfGetResponseTransmitted_Type=Counter32
_BbIfGetResponseTransmitted_Object=MibTableColumn
bbIfGetResponseTransmitted=_BbIfGetResponseTransmitted_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,8),_BbIfGetResponseTransmitted_Type())
bbIfGetResponseTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfGetResponseTransmitted.setStatus(_A)
_BbIfGetRequestTransmitted_Type=Counter32
_BbIfGetRequestTransmitted_Object=MibTableColumn
bbIfGetRequestTransmitted=_BbIfGetRequestTransmitted_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,9),_BbIfGetRequestTransmitted_Type())
bbIfGetRequestTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfGetRequestTransmitted.setStatus(_A)
_BbIfTrapTransmitted_Type=Counter32
_BbIfTrapTransmitted_Object=MibTableColumn
bbIfTrapTransmitted=_BbIfTrapTransmitted_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,10),_BbIfTrapTransmitted_Type())
bbIfTrapTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfTrapTransmitted.setStatus(_A)
_BbIfInvalidPDUReceived_Type=Counter32
_BbIfInvalidPDUReceived_Object=MibTableColumn
bbIfInvalidPDUReceived=_BbIfInvalidPDUReceived_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,11),_BbIfInvalidPDUReceived_Type())
bbIfInvalidPDUReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfInvalidPDUReceived.setStatus(_A)
_BbIfAsn1ParseError_Type=Counter32
_BbIfAsn1ParseError_Object=MibTableColumn
bbIfAsn1ParseError=_BbIfAsn1ParseError_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,12),_BbIfAsn1ParseError_Type())
bbIfAsn1ParseError.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfAsn1ParseError.setStatus(_A)
_BbIfNoSuchNameError_Type=Counter32
_BbIfNoSuchNameError_Object=MibTableColumn
bbIfNoSuchNameError=_BbIfNoSuchNameError_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,13),_BbIfNoSuchNameError_Type())
bbIfNoSuchNameError.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfNoSuchNameError.setStatus(_A)
_BbIfTooBigError_Type=Counter32
_BbIfTooBigError_Object=MibTableColumn
bbIfTooBigError=_BbIfTooBigError_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,14),_BbIfTooBigError_Type())
bbIfTooBigError.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfTooBigError.setStatus(_A)
class _BbIfSigCntClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('resetCounters',2)))
_BbIfSigCntClrButton_Type.__name__=_C
_BbIfSigCntClrButton_Object=MibTableColumn
bbIfSigCntClrButton=_BbIfSigCntClrButton_Object((1,3,6,1,4,1,351,110,5,2,6,4,2,1,1,15),_BbIfSigCntClrButton_Type())
bbIfSigCntClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:bbIfSigCntClrButton.setStatus(_A)
_CwbIlmiMIBConformance_ObjectIdentity=ObjectIdentity
cwbIlmiMIBConformance=_CwbIlmiMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,33,2))
_CwbIlmiMIBGroups_ObjectIdentity=ObjectIdentity
cwbIlmiMIBGroups=_CwbIlmiMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,33,2,1))
_CwbIlmiMIBCompliances_ObjectIdentity=ObjectIdentity
cwbIlmiMIBCompliances=_CwbIlmiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,33,2,2))
cwbIlmiConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,33,2,1,1))
cwbIlmiConfGroup.setObjects(*((_B,_H),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cwbIlmiConfGroup.setStatus(_A)
cwbIlmiStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,33,2,1,2))
cwbIlmiStatsGroup.setObjects(*((_B,_I),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cwbIlmiStatsGroup.setStatus(_A)
cwbIlmiCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,33,2,2,1))
cwbIlmiCompliance.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:cwbIlmiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bbIfCnfSigILMIGrp':bbIfCnfSigILMIGrp,'bbIfCnfSigILMIGrpTable':bbIfCnfSigILMIGrpTable,'bbIfCnfSigILMIGrpEntry':bbIfCnfSigILMIGrpEntry,_H:bbIfSigPortNum,_K:bbIfIlmiEnable,_L:bbIfSignallingProtocolType,_M:bbIfSignallingVpi,_N:bbIfSignallingVci,_O:bbIfAddrPrefix,_P:bbIfCustomerId,_Q:bbIfProtocolRevNo,_R:bbIfIlmiTrapEnable,_S:bbIfMinTrapInterval,_T:bbIfKeepAlivePollingEnable,_U:bbIfErrorThresholdN491,_V:bbIfEventThresholdN492,_W:bbIfPollingIntervalT491,_X:bbIfMinEnquiryIntervalT493,_Y:bbIfAddrRegEnable,'bbIfCntSigILMIGrp':bbIfCntSigILMIGrp,'bbIfCntSigILMIGrpTable':bbIfCntSigILMIGrpTable,'bbIfCntSigILMIGrpEntry':bbIfCntSigILMIGrpEntry,_I:sigCntBbIfNum,_Z:bbIfSnmpPduReceived,_a:bbIfGetRequestReceived,_b:bbIfGetNextRequestReceived,_c:bbIfSetRequestReceived,_d:bbIfTrapReceived,_e:bbIfGetResponseReceived,_f:bbIfGetResponseTransmitted,_g:bbIfGetRequestTransmitted,_h:bbIfTrapTransmitted,_i:bbIfInvalidPDUReceived,_j:bbIfAsn1ParseError,_k:bbIfNoSuchNameError,_l:bbIfTooBigError,_m:bbIfSigCntClrButton,'ciscoWanBbifIlmiMIB':ciscoWanBbifIlmiMIB,'cwbIlmiMIBConformance':cwbIlmiMIBConformance,'cwbIlmiMIBGroups':cwbIlmiMIBGroups,_n:cwbIlmiConfGroup,_o:cwbIlmiStatsGroup,'cwbIlmiMIBCompliances':cwbIlmiMIBCompliances,'cwbIlmiCompliance':cwbIlmiCompliance})