_O='jnxWxAppAggrStatsEntry'
_N='jnxWxAsmStatsEntry'
_M='jnxWxVirtEndptIndex'
_L='jnxWxWpEndptIndex'
_K='jnxWxQosClassIndex'
_J='jnxWxQosEndptIndex'
_I='jnxWxAccelAppIndex'
_H='jnxWxAppIndex'
_G='jnxWxAsmIndex'
_F='not-accessible'
_E='JUNIPER-WX-MIB'
_D='jnxWxCommonEventDescr'
_C='JUNIPER-WX-COMMON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxWxCommonEventDescr,=mibBuilder.importSymbols(_C,_D)
jnxWxModules,jnxWxSpecificMib=mibBuilder.importSymbols('JUNIPER-WX-GLOBAL-REG','jnxWxModules','jnxWxSpecificMib')
TcAppName,TcQosIdentifier=mibBuilder.importSymbols('JUNIPER-WX-GLOBAL-TC','TcAppName','TcQosIdentifier')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
jnxWxMibModule=ModuleIdentity((1,3,6,1,4,1,8239,1,1,4))
if mibBuilder.loadTexts:jnxWxMibModule.setRevisions(('2004-05-24 00:00','2003-06-23 00:00','2002-03-28 00:00','2002-03-27 00:00','2001-12-19 12:00'))
_JnxWxMib_ObjectIdentity=ObjectIdentity
jnxWxMib=_JnxWxMib_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1))
if mibBuilder.loadTexts:jnxWxMib.setStatus(_A)
_JnxWxConfMib_ObjectIdentity=ObjectIdentity
jnxWxConfMib=_JnxWxConfMib_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,1))
if mibBuilder.loadTexts:jnxWxConfMib.setStatus(_A)
_JnxWxObjs_ObjectIdentity=ObjectIdentity
jnxWxObjs=_JnxWxObjs_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2))
if mibBuilder.loadTexts:jnxWxObjs.setStatus(_A)
_JnxWxStatsUpdateTime_Type=TimeStamp
_JnxWxStatsUpdateTime_Object=MibScalar
jnxWxStatsUpdateTime=_JnxWxStatsUpdateTime_Object((1,3,6,1,4,1,8239,2,2,1,2,1),_JnxWxStatsUpdateTime_Type())
jnxWxStatsUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsUpdateTime.setStatus(_A)
_JnxWxStatsAsmCount_Type=Integer32
_JnxWxStatsAsmCount_Object=MibScalar
jnxWxStatsAsmCount=_JnxWxStatsAsmCount_Object((1,3,6,1,4,1,8239,2,2,1,2,2),_JnxWxStatsAsmCount_Type())
jnxWxStatsAsmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsAsmCount.setStatus(_A)
_JnxWxStatsAppCount_Type=Integer32
_JnxWxStatsAppCount_Object=MibScalar
jnxWxStatsAppCount=_JnxWxStatsAppCount_Object((1,3,6,1,4,1,8239,2,2,1,2,3),_JnxWxStatsAppCount_Type())
jnxWxStatsAppCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsAppCount.setStatus(_A)
_JnxWxSysStats_ObjectIdentity=ObjectIdentity
jnxWxSysStats=_JnxWxSysStats_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,4))
if mibBuilder.loadTexts:jnxWxSysStats.setStatus(_A)
_JnxWxSysStatsBytesInAe_Type=Counter64
_JnxWxSysStatsBytesInAe_Object=MibScalar
jnxWxSysStatsBytesInAe=_JnxWxSysStatsBytesInAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,1),_JnxWxSysStatsBytesInAe_Type())
jnxWxSysStatsBytesInAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesInAe.setStatus(_A)
_JnxWxSysStatsBytesOutAe_Type=Counter64
_JnxWxSysStatsBytesOutAe_Object=MibScalar
jnxWxSysStatsBytesOutAe=_JnxWxSysStatsBytesOutAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,2),_JnxWxSysStatsBytesOutAe_Type())
jnxWxSysStatsBytesOutAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesOutAe.setStatus(_A)
_JnxWxSysStatsPktsInAe_Type=Counter64
_JnxWxSysStatsPktsInAe_Object=MibScalar
jnxWxSysStatsPktsInAe=_JnxWxSysStatsPktsInAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,3),_JnxWxSysStatsPktsInAe_Type())
jnxWxSysStatsPktsInAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsInAe.setStatus(_A)
_JnxWxSysStatsPktsOutAe_Type=Counter64
_JnxWxSysStatsPktsOutAe_Object=MibScalar
jnxWxSysStatsPktsOutAe=_JnxWxSysStatsPktsOutAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,4),_JnxWxSysStatsPktsOutAe_Type())
jnxWxSysStatsPktsOutAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsOutAe.setStatus(_A)
_JnxWxSysStatsBytesOutOob_Type=Counter64
_JnxWxSysStatsBytesOutOob_Object=MibScalar
jnxWxSysStatsBytesOutOob=_JnxWxSysStatsBytesOutOob_Object((1,3,6,1,4,1,8239,2,2,1,2,4,5),_JnxWxSysStatsBytesOutOob_Type())
jnxWxSysStatsBytesOutOob.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesOutOob.setStatus(_A)
_JnxWxSysStatsBytesPtNoAe_Type=Counter64
_JnxWxSysStatsBytesPtNoAe_Object=MibScalar
jnxWxSysStatsBytesPtNoAe=_JnxWxSysStatsBytesPtNoAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,6),_JnxWxSysStatsBytesPtNoAe_Type())
jnxWxSysStatsBytesPtNoAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesPtNoAe.setStatus(_A)
_JnxWxSysStatsPktsPtNoAe_Type=Counter64
_JnxWxSysStatsPktsPtNoAe_Object=MibScalar
jnxWxSysStatsPktsPtNoAe=_JnxWxSysStatsPktsPtNoAe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,7),_JnxWxSysStatsPktsPtNoAe_Type())
jnxWxSysStatsPktsPtNoAe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsPtNoAe.setStatus(_A)
_JnxWxSysStatsBytesPtFilter_Type=Counter64
_JnxWxSysStatsBytesPtFilter_Object=MibScalar
jnxWxSysStatsBytesPtFilter=_JnxWxSysStatsBytesPtFilter_Object((1,3,6,1,4,1,8239,2,2,1,2,4,8),_JnxWxSysStatsBytesPtFilter_Type())
jnxWxSysStatsBytesPtFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesPtFilter.setStatus(_A)
_JnxWxSysStatsPktsPtFilter_Type=Counter64
_JnxWxSysStatsPktsPtFilter_Object=MibScalar
jnxWxSysStatsPktsPtFilter=_JnxWxSysStatsPktsPtFilter_Object((1,3,6,1,4,1,8239,2,2,1,2,4,9),_JnxWxSysStatsPktsPtFilter_Type())
jnxWxSysStatsPktsPtFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsPtFilter.setStatus(_A)
_JnxWxSysStatsBytesOfPt_Type=Counter64
_JnxWxSysStatsBytesOfPt_Object=MibScalar
jnxWxSysStatsBytesOfPt=_JnxWxSysStatsBytesOfPt_Object((1,3,6,1,4,1,8239,2,2,1,2,4,10),_JnxWxSysStatsBytesOfPt_Type())
jnxWxSysStatsBytesOfPt.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesOfPt.setStatus(_A)
_JnxWxSysStatsPktsOfPt_Type=Counter64
_JnxWxSysStatsPktsOfPt_Object=MibScalar
jnxWxSysStatsPktsOfPt=_JnxWxSysStatsPktsOfPt_Object((1,3,6,1,4,1,8239,2,2,1,2,4,11),_JnxWxSysStatsPktsOfPt_Type())
jnxWxSysStatsPktsOfPt.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsOfPt.setStatus(_A)
_JnxWxSysStatsBytesTpIn_Type=Counter64
_JnxWxSysStatsBytesTpIn_Object=MibScalar
jnxWxSysStatsBytesTpIn=_JnxWxSysStatsBytesTpIn_Object((1,3,6,1,4,1,8239,2,2,1,2,4,12),_JnxWxSysStatsBytesTpIn_Type())
jnxWxSysStatsBytesTpIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesTpIn.setStatus(_A)
_JnxWxSysStatsPktsTpIn_Type=Counter64
_JnxWxSysStatsPktsTpIn_Object=MibScalar
jnxWxSysStatsPktsTpIn=_JnxWxSysStatsPktsTpIn_Object((1,3,6,1,4,1,8239,2,2,1,2,4,13),_JnxWxSysStatsPktsTpIn_Type())
jnxWxSysStatsPktsTpIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsTpIn.setStatus(_A)
_JnxWxSysStatsBytesTpOut_Type=Counter64
_JnxWxSysStatsBytesTpOut_Object=MibScalar
jnxWxSysStatsBytesTpOut=_JnxWxSysStatsBytesTpOut_Object((1,3,6,1,4,1,8239,2,2,1,2,4,14),_JnxWxSysStatsBytesTpOut_Type())
jnxWxSysStatsBytesTpOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesTpOut.setStatus(_A)
_JnxWxSysStatsPktsTpOut_Type=Counter64
_JnxWxSysStatsPktsTpOut_Object=MibScalar
jnxWxSysStatsPktsTpOut=_JnxWxSysStatsPktsTpOut_Object((1,3,6,1,4,1,8239,2,2,1,2,4,15),_JnxWxSysStatsPktsTpOut_Type())
jnxWxSysStatsPktsTpOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsTpOut.setStatus(_A)
_JnxWxSysStatsBytesTpPt_Type=Counter64
_JnxWxSysStatsBytesTpPt_Object=MibScalar
jnxWxSysStatsBytesTpPt=_JnxWxSysStatsBytesTpPt_Object((1,3,6,1,4,1,8239,2,2,1,2,4,16),_JnxWxSysStatsBytesTpPt_Type())
jnxWxSysStatsBytesTpPt.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesTpPt.setStatus(_A)
_JnxWxSysStatsPktsTpPt_Type=Counter64
_JnxWxSysStatsPktsTpPt_Object=MibScalar
jnxWxSysStatsPktsTpPt=_JnxWxSysStatsPktsTpPt_Object((1,3,6,1,4,1,8239,2,2,1,2,4,17),_JnxWxSysStatsPktsTpPt_Type())
jnxWxSysStatsPktsTpPt.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsTpPt.setStatus(_A)
_JnxWxSysStatsPeakRdn_Type=Unsigned32
_JnxWxSysStatsPeakRdn_Object=MibScalar
jnxWxSysStatsPeakRdn=_JnxWxSysStatsPeakRdn_Object((1,3,6,1,4,1,8239,2,2,1,2,4,18),_JnxWxSysStatsPeakRdn_Type())
jnxWxSysStatsPeakRdn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPeakRdn.setStatus(_A)
_JnxWxSysStatsThruputIn_Type=Gauge32
_JnxWxSysStatsThruputIn_Object=MibScalar
jnxWxSysStatsThruputIn=_JnxWxSysStatsThruputIn_Object((1,3,6,1,4,1,8239,2,2,1,2,4,19),_JnxWxSysStatsThruputIn_Type())
jnxWxSysStatsThruputIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsThruputIn.setStatus(_A)
_JnxWxSysStatsThruputOut_Type=Gauge32
_JnxWxSysStatsThruputOut_Object=MibScalar
jnxWxSysStatsThruputOut=_JnxWxSysStatsThruputOut_Object((1,3,6,1,4,1,8239,2,2,1,2,4,20),_JnxWxSysStatsThruputOut_Type())
jnxWxSysStatsThruputOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsThruputOut.setStatus(_A)
_JnxWxSysStatsBytesInRe_Type=Counter64
_JnxWxSysStatsBytesInRe_Object=MibScalar
jnxWxSysStatsBytesInRe=_JnxWxSysStatsBytesInRe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,21),_JnxWxSysStatsBytesInRe_Type())
jnxWxSysStatsBytesInRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesInRe.setStatus(_A)
_JnxWxSysStatsBytesOutRe_Type=Counter64
_JnxWxSysStatsBytesOutRe_Object=MibScalar
jnxWxSysStatsBytesOutRe=_JnxWxSysStatsBytesOutRe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,22),_JnxWxSysStatsBytesOutRe_Type())
jnxWxSysStatsBytesOutRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsBytesOutRe.setStatus(_A)
_JnxWxSysStatsPktsInRe_Type=Counter64
_JnxWxSysStatsPktsInRe_Object=MibScalar
jnxWxSysStatsPktsInRe=_JnxWxSysStatsPktsInRe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,23),_JnxWxSysStatsPktsInRe_Type())
jnxWxSysStatsPktsInRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsInRe.setStatus(_A)
_JnxWxSysStatsPktsOutRe_Type=Counter64
_JnxWxSysStatsPktsOutRe_Object=MibScalar
jnxWxSysStatsPktsOutRe=_JnxWxSysStatsPktsOutRe_Object((1,3,6,1,4,1,8239,2,2,1,2,4,24),_JnxWxSysStatsPktsOutRe_Type())
jnxWxSysStatsPktsOutRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktsOutRe.setStatus(_A)
_JnxWxSysStatsPktSizeIn1_Type=Counter64
_JnxWxSysStatsPktSizeIn1_Object=MibScalar
jnxWxSysStatsPktSizeIn1=_JnxWxSysStatsPktSizeIn1_Object((1,3,6,1,4,1,8239,2,2,1,2,4,25),_JnxWxSysStatsPktSizeIn1_Type())
jnxWxSysStatsPktSizeIn1.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn1.setStatus(_A)
_JnxWxSysStatsPktSizeIn2_Type=Counter64
_JnxWxSysStatsPktSizeIn2_Object=MibScalar
jnxWxSysStatsPktSizeIn2=_JnxWxSysStatsPktSizeIn2_Object((1,3,6,1,4,1,8239,2,2,1,2,4,26),_JnxWxSysStatsPktSizeIn2_Type())
jnxWxSysStatsPktSizeIn2.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn2.setStatus(_A)
_JnxWxSysStatsPktSizeIn3_Type=Counter64
_JnxWxSysStatsPktSizeIn3_Object=MibScalar
jnxWxSysStatsPktSizeIn3=_JnxWxSysStatsPktSizeIn3_Object((1,3,6,1,4,1,8239,2,2,1,2,4,27),_JnxWxSysStatsPktSizeIn3_Type())
jnxWxSysStatsPktSizeIn3.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn3.setStatus(_A)
_JnxWxSysStatsPktSizeIn4_Type=Counter64
_JnxWxSysStatsPktSizeIn4_Object=MibScalar
jnxWxSysStatsPktSizeIn4=_JnxWxSysStatsPktSizeIn4_Object((1,3,6,1,4,1,8239,2,2,1,2,4,28),_JnxWxSysStatsPktSizeIn4_Type())
jnxWxSysStatsPktSizeIn4.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn4.setStatus(_A)
_JnxWxSysStatsPktSizeIn5_Type=Counter64
_JnxWxSysStatsPktSizeIn5_Object=MibScalar
jnxWxSysStatsPktSizeIn5=_JnxWxSysStatsPktSizeIn5_Object((1,3,6,1,4,1,8239,2,2,1,2,4,29),_JnxWxSysStatsPktSizeIn5_Type())
jnxWxSysStatsPktSizeIn5.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn5.setStatus(_A)
_JnxWxSysStatsPktSizeIn6_Type=Counter64
_JnxWxSysStatsPktSizeIn6_Object=MibScalar
jnxWxSysStatsPktSizeIn6=_JnxWxSysStatsPktSizeIn6_Object((1,3,6,1,4,1,8239,2,2,1,2,4,30),_JnxWxSysStatsPktSizeIn6_Type())
jnxWxSysStatsPktSizeIn6.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeIn6.setStatus(_A)
_JnxWxSysStatsPktSizeOut1_Type=Counter64
_JnxWxSysStatsPktSizeOut1_Object=MibScalar
jnxWxSysStatsPktSizeOut1=_JnxWxSysStatsPktSizeOut1_Object((1,3,6,1,4,1,8239,2,2,1,2,4,31),_JnxWxSysStatsPktSizeOut1_Type())
jnxWxSysStatsPktSizeOut1.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut1.setStatus(_A)
_JnxWxSysStatsPktSizeOut2_Type=Counter64
_JnxWxSysStatsPktSizeOut2_Object=MibScalar
jnxWxSysStatsPktSizeOut2=_JnxWxSysStatsPktSizeOut2_Object((1,3,6,1,4,1,8239,2,2,1,2,4,32),_JnxWxSysStatsPktSizeOut2_Type())
jnxWxSysStatsPktSizeOut2.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut2.setStatus(_A)
_JnxWxSysStatsPktSizeOut3_Type=Counter64
_JnxWxSysStatsPktSizeOut3_Object=MibScalar
jnxWxSysStatsPktSizeOut3=_JnxWxSysStatsPktSizeOut3_Object((1,3,6,1,4,1,8239,2,2,1,2,4,33),_JnxWxSysStatsPktSizeOut3_Type())
jnxWxSysStatsPktSizeOut3.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut3.setStatus(_A)
_JnxWxSysStatsPktSizeOut4_Type=Counter64
_JnxWxSysStatsPktSizeOut4_Object=MibScalar
jnxWxSysStatsPktSizeOut4=_JnxWxSysStatsPktSizeOut4_Object((1,3,6,1,4,1,8239,2,2,1,2,4,34),_JnxWxSysStatsPktSizeOut4_Type())
jnxWxSysStatsPktSizeOut4.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut4.setStatus(_A)
_JnxWxSysStatsPktSizeOut5_Type=Counter64
_JnxWxSysStatsPktSizeOut5_Object=MibScalar
jnxWxSysStatsPktSizeOut5=_JnxWxSysStatsPktSizeOut5_Object((1,3,6,1,4,1,8239,2,2,1,2,4,35),_JnxWxSysStatsPktSizeOut5_Type())
jnxWxSysStatsPktSizeOut5.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut5.setStatus(_A)
_JnxWxSysStatsPktSizeOut6_Type=Counter64
_JnxWxSysStatsPktSizeOut6_Object=MibScalar
jnxWxSysStatsPktSizeOut6=_JnxWxSysStatsPktSizeOut6_Object((1,3,6,1,4,1,8239,2,2,1,2,4,36),_JnxWxSysStatsPktSizeOut6_Type())
jnxWxSysStatsPktSizeOut6.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxSysStatsPktSizeOut6.setStatus(_A)
_JnxWxAsm_ObjectIdentity=ObjectIdentity
jnxWxAsm=_JnxWxAsm_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,5))
if mibBuilder.loadTexts:jnxWxAsm.setStatus(_A)
_JnxWxAsmTable_Object=MibTable
jnxWxAsmTable=_JnxWxAsmTable_Object((1,3,6,1,4,1,8239,2,2,1,2,5,1))
if mibBuilder.loadTexts:jnxWxAsmTable.setStatus(_A)
_JnxWxAsmEntry_Object=MibTableRow
jnxWxAsmEntry=_JnxWxAsmEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,5,1,1))
jnxWxAsmEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:jnxWxAsmEntry.setStatus(_A)
_JnxWxAsmIndex_Type=Integer32
_JnxWxAsmIndex_Object=MibTableColumn
jnxWxAsmIndex=_JnxWxAsmIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,5,1,1,1),_JnxWxAsmIndex_Type())
jnxWxAsmIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxAsmIndex.setStatus(_A)
_JnxWxAsmIpAddress_Type=IpAddress
_JnxWxAsmIpAddress_Object=MibTableColumn
jnxWxAsmIpAddress=_JnxWxAsmIpAddress_Object((1,3,6,1,4,1,8239,2,2,1,2,5,1,1,2),_JnxWxAsmIpAddress_Type())
jnxWxAsmIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAsmIpAddress.setStatus(_A)
_JnxWxAsmStatsTable_Object=MibTable
jnxWxAsmStatsTable=_JnxWxAsmStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2))
if mibBuilder.loadTexts:jnxWxAsmStatsTable.setStatus(_A)
_JnxWxAsmStatsEntry_Object=MibTableRow
jnxWxAsmStatsEntry=_JnxWxAsmStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2,1))
if mibBuilder.loadTexts:jnxWxAsmStatsEntry.setStatus(_A)
_JnxWxAsmStatsPktsIn_Type=Counter64
_JnxWxAsmStatsPktsIn_Object=MibTableColumn
jnxWxAsmStatsPktsIn=_JnxWxAsmStatsPktsIn_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2,1,1),_JnxWxAsmStatsPktsIn_Type())
jnxWxAsmStatsPktsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAsmStatsPktsIn.setStatus(_A)
_JnxWxAsmStatsPktsOut_Type=Counter64
_JnxWxAsmStatsPktsOut_Object=MibTableColumn
jnxWxAsmStatsPktsOut=_JnxWxAsmStatsPktsOut_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2,1,2),_JnxWxAsmStatsPktsOut_Type())
jnxWxAsmStatsPktsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAsmStatsPktsOut.setStatus(_A)
_JnxWxAsmStatsBytesIn_Type=Counter64
_JnxWxAsmStatsBytesIn_Object=MibTableColumn
jnxWxAsmStatsBytesIn=_JnxWxAsmStatsBytesIn_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2,1,3),_JnxWxAsmStatsBytesIn_Type())
jnxWxAsmStatsBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAsmStatsBytesIn.setStatus(_A)
_JnxWxAsmStatsBytesOut_Type=Counter64
_JnxWxAsmStatsBytesOut_Object=MibTableColumn
jnxWxAsmStatsBytesOut=_JnxWxAsmStatsBytesOut_Object((1,3,6,1,4,1,8239,2,2,1,2,5,2,1,4),_JnxWxAsmStatsBytesOut_Type())
jnxWxAsmStatsBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAsmStatsBytesOut.setStatus(_A)
_JnxWxVirtEndptTable_Object=MibTable
jnxWxVirtEndptTable=_JnxWxVirtEndptTable_Object((1,3,6,1,4,1,8239,2,2,1,2,5,3))
if mibBuilder.loadTexts:jnxWxVirtEndptTable.setStatus(_A)
_JnxWxVirtEndptEntry_Object=MibTableRow
jnxWxVirtEndptEntry=_JnxWxVirtEndptEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,5,3,1))
jnxWxVirtEndptEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:jnxWxVirtEndptEntry.setStatus(_A)
_JnxWxVirtEndptIndex_Type=Integer32
_JnxWxVirtEndptIndex_Object=MibTableColumn
jnxWxVirtEndptIndex=_JnxWxVirtEndptIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,5,3,1,1),_JnxWxVirtEndptIndex_Type())
jnxWxVirtEndptIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxVirtEndptIndex.setStatus(_A)
_JnxWxVirtEndptName_Type=TcAppName
_JnxWxVirtEndptName_Object=MibTableColumn
jnxWxVirtEndptName=_JnxWxVirtEndptName_Object((1,3,6,1,4,1,8239,2,2,1,2,5,3,1,2),_JnxWxVirtEndptName_Type())
jnxWxVirtEndptName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxVirtEndptName.setStatus(_A)
_JnxWxVirtEndptSubnetCount_Type=Integer32
_JnxWxVirtEndptSubnetCount_Object=MibTableColumn
jnxWxVirtEndptSubnetCount=_JnxWxVirtEndptSubnetCount_Object((1,3,6,1,4,1,8239,2,2,1,2,5,3,1,3),_JnxWxVirtEndptSubnetCount_Type())
jnxWxVirtEndptSubnetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxVirtEndptSubnetCount.setStatus(_A)
_JnxWxApp_ObjectIdentity=ObjectIdentity
jnxWxApp=_JnxWxApp_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,6))
if mibBuilder.loadTexts:jnxWxApp.setStatus(_A)
_JnxWxAppTable_Object=MibTable
jnxWxAppTable=_JnxWxAppTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,1))
if mibBuilder.loadTexts:jnxWxAppTable.setStatus(_A)
_JnxWxAppEntry_Object=MibTableRow
jnxWxAppEntry=_JnxWxAppEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,1,1))
jnxWxAppEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:jnxWxAppEntry.setStatus(_A)
_JnxWxAppIndex_Type=Integer32
_JnxWxAppIndex_Object=MibTableColumn
jnxWxAppIndex=_JnxWxAppIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,6,1,1,1),_JnxWxAppIndex_Type())
jnxWxAppIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxAppIndex.setStatus(_A)
_JnxWxAppAppName_Type=TcAppName
_JnxWxAppAppName_Object=MibTableColumn
jnxWxAppAppName=_JnxWxAppAppName_Object((1,3,6,1,4,1,8239,2,2,1,2,6,1,1,2),_JnxWxAppAppName_Type())
jnxWxAppAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppAppName.setStatus(_A)
_JnxWxAppStatsTable_Object=MibTable
jnxWxAppStatsTable=_JnxWxAppStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2))
if mibBuilder.loadTexts:jnxWxAppStatsTable.setStatus(_A)
_JnxWxAppStatsEntry_Object=MibTableRow
jnxWxAppStatsEntry=_JnxWxAppStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1))
jnxWxAppStatsEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:jnxWxAppStatsEntry.setStatus(_A)
_JnxWxAppStatsBytesIn_Type=Counter64
_JnxWxAppStatsBytesIn_Object=MibTableColumn
jnxWxAppStatsBytesIn=_JnxWxAppStatsBytesIn_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,1),_JnxWxAppStatsBytesIn_Type())
jnxWxAppStatsBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsBytesIn.setStatus(_A)
_JnxWxAppStatsBytesOut_Type=Counter64
_JnxWxAppStatsBytesOut_Object=MibTableColumn
jnxWxAppStatsBytesOut=_JnxWxAppStatsBytesOut_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,2),_JnxWxAppStatsBytesOut_Type())
jnxWxAppStatsBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsBytesOut.setStatus(_A)
_JnxWxAppStatsBytesInPercent_Type=Gauge32
_JnxWxAppStatsBytesInPercent_Object=MibTableColumn
jnxWxAppStatsBytesInPercent=_JnxWxAppStatsBytesInPercent_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,3),_JnxWxAppStatsBytesInPercent_Type())
jnxWxAppStatsBytesInPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsBytesInPercent.setStatus(_A)
_JnxWxAppStatsAppName_Type=TcAppName
_JnxWxAppStatsAppName_Object=MibTableColumn
jnxWxAppStatsAppName=_JnxWxAppStatsAppName_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,4),_JnxWxAppStatsAppName_Type())
jnxWxAppStatsAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsAppName.setStatus(_A)
_JnxWxAppStatsAccelBytesIn_Type=Counter64
_JnxWxAppStatsAccelBytesIn_Object=MibTableColumn
jnxWxAppStatsAccelBytesIn=_JnxWxAppStatsAccelBytesIn_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,5),_JnxWxAppStatsAccelBytesIn_Type())
jnxWxAppStatsAccelBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsAccelBytesIn.setStatus(_A)
_JnxWxAppStatsActiveSessionTime_Type=Counter64
_JnxWxAppStatsActiveSessionTime_Object=MibTableColumn
jnxWxAppStatsActiveSessionTime=_JnxWxAppStatsActiveSessionTime_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,6),_JnxWxAppStatsActiveSessionTime_Type())
jnxWxAppStatsActiveSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsActiveSessionTime.setStatus(_A)
_JnxWxAppStatsEstBoostBytes_Type=Counter64
_JnxWxAppStatsEstBoostBytes_Object=MibTableColumn
jnxWxAppStatsEstBoostBytes=_JnxWxAppStatsEstBoostBytes_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,7),_JnxWxAppStatsEstBoostBytes_Type())
jnxWxAppStatsEstBoostBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsEstBoostBytes.setStatus(_A)
_JnxWxAppStatsBytesOutWxc_Type=Counter64
_JnxWxAppStatsBytesOutWxc_Object=MibTableColumn
jnxWxAppStatsBytesOutWxc=_JnxWxAppStatsBytesOutWxc_Object((1,3,6,1,4,1,8239,2,2,1,2,6,2,1,8),_JnxWxAppStatsBytesOutWxc_Type())
jnxWxAppStatsBytesOutWxc.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppStatsBytesOutWxc.setStatus(_A)
_JnxWxAppAggrStatsTable_Object=MibTable
jnxWxAppAggrStatsTable=_JnxWxAppAggrStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,3))
if mibBuilder.loadTexts:jnxWxAppAggrStatsTable.setStatus(_A)
_JnxWxAppAggrStatsEntry_Object=MibTableRow
jnxWxAppAggrStatsEntry=_JnxWxAppAggrStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,3,1))
if mibBuilder.loadTexts:jnxWxAppAggrStatsEntry.setStatus(_A)
_JnxWxAppAggrStatsBytesInRe_Type=Counter64
_JnxWxAppAggrStatsBytesInRe_Object=MibTableColumn
jnxWxAppAggrStatsBytesInRe=_JnxWxAppAggrStatsBytesInRe_Object((1,3,6,1,4,1,8239,2,2,1,2,6,3,1,1),_JnxWxAppAggrStatsBytesInRe_Type())
jnxWxAppAggrStatsBytesInRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppAggrStatsBytesInRe.setStatus(_A)
_JnxWxAppAggrStatsBytesOutRe_Type=Counter64
_JnxWxAppAggrStatsBytesOutRe_Object=MibTableColumn
jnxWxAppAggrStatsBytesOutRe=_JnxWxAppAggrStatsBytesOutRe_Object((1,3,6,1,4,1,8239,2,2,1,2,6,3,1,2),_JnxWxAppAggrStatsBytesOutRe_Type())
jnxWxAppAggrStatsBytesOutRe.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppAggrStatsBytesOutRe.setStatus(_A)
_JnxWxAppAggrStatsBytesInPercent_Type=Gauge32
_JnxWxAppAggrStatsBytesInPercent_Object=MibTableColumn
jnxWxAppAggrStatsBytesInPercent=_JnxWxAppAggrStatsBytesInPercent_Object((1,3,6,1,4,1,8239,2,2,1,2,6,3,1,3),_JnxWxAppAggrStatsBytesInPercent_Type())
jnxWxAppAggrStatsBytesInPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAppAggrStatsBytesInPercent.setStatus(_A)
_JnxWxWanStatsTable_Object=MibTable
jnxWxWanStatsTable=_JnxWxWanStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,4))
if mibBuilder.loadTexts:jnxWxWanStatsTable.setStatus(_A)
_JnxWxWanStatsEntry_Object=MibTableRow
jnxWxWanStatsEntry=_JnxWxWanStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,4,1))
jnxWxWanStatsEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:jnxWxWanStatsEntry.setStatus(_A)
_JnxWxWanStatsBytesToWan_Type=Counter64
_JnxWxWanStatsBytesToWan_Object=MibTableColumn
jnxWxWanStatsBytesToWan=_JnxWxWanStatsBytesToWan_Object((1,3,6,1,4,1,8239,2,2,1,2,6,4,1,1),_JnxWxWanStatsBytesToWan_Type())
jnxWxWanStatsBytesToWan.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWanStatsBytesToWan.setStatus(_A)
_JnxWxWanStatsBytesFromWan_Type=Counter64
_JnxWxWanStatsBytesFromWan_Object=MibTableColumn
jnxWxWanStatsBytesFromWan=_JnxWxWanStatsBytesFromWan_Object((1,3,6,1,4,1,8239,2,2,1,2,6,4,1,2),_JnxWxWanStatsBytesFromWan_Type())
jnxWxWanStatsBytesFromWan.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWanStatsBytesFromWan.setStatus(_A)
_JnxWxAccelAppNameTable_Object=MibTable
jnxWxAccelAppNameTable=_JnxWxAccelAppNameTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,5))
if mibBuilder.loadTexts:jnxWxAccelAppNameTable.setStatus(_A)
_JnxWxAccelAppNameEntry_Object=MibTableRow
jnxWxAccelAppNameEntry=_JnxWxAccelAppNameEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,5,1))
jnxWxAccelAppNameEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:jnxWxAccelAppNameEntry.setStatus(_A)
_JnxWxAccelAppIndex_Type=Integer32
_JnxWxAccelAppIndex_Object=MibTableColumn
jnxWxAccelAppIndex=_JnxWxAccelAppIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,6,5,1,1),_JnxWxAccelAppIndex_Type())
jnxWxAccelAppIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxAccelAppIndex.setStatus(_A)
_JnxWxAccelAppName_Type=TcAppName
_JnxWxAccelAppName_Object=MibTableColumn
jnxWxAccelAppName=_JnxWxAccelAppName_Object((1,3,6,1,4,1,8239,2,2,1,2,6,5,1,2),_JnxWxAccelAppName_Type())
jnxWxAccelAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAccelAppName.setStatus(_A)
_JnxWxAccelAppStatsTable_Object=MibTable
jnxWxAccelAppStatsTable=_JnxWxAccelAppStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,6,6))
if mibBuilder.loadTexts:jnxWxAccelAppStatsTable.setStatus(_A)
_JnxWxAccelAppStatsEntry_Object=MibTableRow
jnxWxAccelAppStatsEntry=_JnxWxAccelAppStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,6,6,1))
jnxWxAccelAppStatsEntry.setIndexNames((0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:jnxWxAccelAppStatsEntry.setStatus(_A)
_JnxWxAccelAppTimeWithAccel_Type=Unsigned32
_JnxWxAccelAppTimeWithAccel_Object=MibTableColumn
jnxWxAccelAppTimeWithAccel=_JnxWxAccelAppTimeWithAccel_Object((1,3,6,1,4,1,8239,2,2,1,2,6,6,1,3),_JnxWxAccelAppTimeWithAccel_Type())
jnxWxAccelAppTimeWithAccel.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAccelAppTimeWithAccel.setStatus(_A)
_JnxWxAccelAppTimeWithoutAccel_Type=Unsigned32
_JnxWxAccelAppTimeWithoutAccel_Object=MibTableColumn
jnxWxAccelAppTimeWithoutAccel=_JnxWxAccelAppTimeWithoutAccel_Object((1,3,6,1,4,1,8239,2,2,1,2,6,6,1,4),_JnxWxAccelAppTimeWithoutAccel_Type())
jnxWxAccelAppTimeWithoutAccel.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxAccelAppTimeWithoutAccel.setStatus(_A)
_JnxWxBurstStats_ObjectIdentity=ObjectIdentity
jnxWxBurstStats=_JnxWxBurstStats_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,7))
if mibBuilder.loadTexts:jnxWxBurstStats.setStatus(_A)
_JnxWxBurstStatsStartTime_Type=Integer32
_JnxWxBurstStatsStartTime_Object=MibScalar
jnxWxBurstStatsStartTime=_JnxWxBurstStatsStartTime_Object((1,3,6,1,4,1,8239,2,2,1,2,7,1),_JnxWxBurstStatsStartTime_Type())
jnxWxBurstStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxBurstStatsStartTime.setStatus(_A)
_JnxWxBurstStatsBpsIn_Type=Gauge32
_JnxWxBurstStatsBpsIn_Object=MibScalar
jnxWxBurstStatsBpsIn=_JnxWxBurstStatsBpsIn_Object((1,3,6,1,4,1,8239,2,2,1,2,7,2),_JnxWxBurstStatsBpsIn_Type())
jnxWxBurstStatsBpsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxBurstStatsBpsIn.setStatus(_A)
_JnxWxBurstStatsBpsOut_Type=Gauge32
_JnxWxBurstStatsBpsOut_Object=MibScalar
jnxWxBurstStatsBpsOut=_JnxWxBurstStatsBpsOut_Object((1,3,6,1,4,1,8239,2,2,1,2,7,3),_JnxWxBurstStatsBpsOut_Type())
jnxWxBurstStatsBpsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxBurstStatsBpsOut.setStatus(_A)
_JnxWxBurstStatsBpsPt_Type=Gauge32
_JnxWxBurstStatsBpsPt_Object=MibScalar
jnxWxBurstStatsBpsPt=_JnxWxBurstStatsBpsPt_Object((1,3,6,1,4,1,8239,2,2,1,2,7,4),_JnxWxBurstStatsBpsPt_Type())
jnxWxBurstStatsBpsPt.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxBurstStatsBpsPt.setStatus(_A)
_JnxWxStatsAccelAppCount_Type=Integer32
_JnxWxStatsAccelAppCount_Object=MibScalar
jnxWxStatsAccelAppCount=_JnxWxStatsAccelAppCount_Object((1,3,6,1,4,1,8239,2,2,1,2,8),_JnxWxStatsAccelAppCount_Type())
jnxWxStatsAccelAppCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsAccelAppCount.setStatus(_A)
_JnxWxStatsVirtEndptCount_Type=Integer32
_JnxWxStatsVirtEndptCount_Object=MibScalar
jnxWxStatsVirtEndptCount=_JnxWxStatsVirtEndptCount_Object((1,3,6,1,4,1,8239,2,2,1,2,9),_JnxWxStatsVirtEndptCount_Type())
jnxWxStatsVirtEndptCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsVirtEndptCount.setStatus(_A)
_JnxWxQos_ObjectIdentity=ObjectIdentity
jnxWxQos=_JnxWxQos_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,10))
if mibBuilder.loadTexts:jnxWxQos.setStatus(_A)
_JnxWxQosEndptTable_Object=MibTable
jnxWxQosEndptTable=_JnxWxQosEndptTable_Object((1,3,6,1,4,1,8239,2,2,1,2,10,1))
if mibBuilder.loadTexts:jnxWxQosEndptTable.setStatus(_A)
_JnxWxQosEndptEntry_Object=MibTableRow
jnxWxQosEndptEntry=_JnxWxQosEndptEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,10,1,1))
jnxWxQosEndptEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:jnxWxQosEndptEntry.setStatus(_A)
_JnxWxQosEndptIndex_Type=Integer32
_JnxWxQosEndptIndex_Object=MibTableColumn
jnxWxQosEndptIndex=_JnxWxQosEndptIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,10,1,1,1),_JnxWxQosEndptIndex_Type())
jnxWxQosEndptIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxQosEndptIndex.setStatus(_A)
_JnxWxQosEndptIdentifier_Type=TcQosIdentifier
_JnxWxQosEndptIdentifier_Object=MibTableColumn
jnxWxQosEndptIdentifier=_JnxWxQosEndptIdentifier_Object((1,3,6,1,4,1,8239,2,2,1,2,10,1,1,2),_JnxWxQosEndptIdentifier_Type())
jnxWxQosEndptIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosEndptIdentifier.setStatus(_A)
_JnxWxQosClassTable_Object=MibTable
jnxWxQosClassTable=_JnxWxQosClassTable_Object((1,3,6,1,4,1,8239,2,2,1,2,10,2))
if mibBuilder.loadTexts:jnxWxQosClassTable.setStatus(_A)
_JnxWxQosClassEntry_Object=MibTableRow
jnxWxQosClassEntry=_JnxWxQosClassEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,10,2,1))
jnxWxQosClassEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:jnxWxQosClassEntry.setStatus(_A)
_JnxWxQosClassIndex_Type=Integer32
_JnxWxQosClassIndex_Object=MibTableColumn
jnxWxQosClassIndex=_JnxWxQosClassIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,10,2,1,1),_JnxWxQosClassIndex_Type())
jnxWxQosClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxQosClassIndex.setStatus(_A)
_JnxWxQosClassName_Type=TcQosIdentifier
_JnxWxQosClassName_Object=MibTableColumn
jnxWxQosClassName=_JnxWxQosClassName_Object((1,3,6,1,4,1,8239,2,2,1,2,10,2,1,2),_JnxWxQosClassName_Type())
jnxWxQosClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosClassName.setStatus(_A)
_JnxWxQosStatsTable_Object=MibTable
jnxWxQosStatsTable=_JnxWxQosStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3))
if mibBuilder.loadTexts:jnxWxQosStatsTable.setStatus(_A)
_JnxWxQosStatsEntry_Object=MibTableRow
jnxWxQosStatsEntry=_JnxWxQosStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1))
jnxWxQosStatsEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:jnxWxQosStatsEntry.setStatus(_A)
_JnxWxQosStatsBytesIn_Type=Counter64
_JnxWxQosStatsBytesIn_Object=MibTableColumn
jnxWxQosStatsBytesIn=_JnxWxQosStatsBytesIn_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,3),_JnxWxQosStatsBytesIn_Type())
jnxWxQosStatsBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsBytesIn.setStatus(_A)
_JnxWxQosStatsBytesOut_Type=Counter64
_JnxWxQosStatsBytesOut_Object=MibTableColumn
jnxWxQosStatsBytesOut=_JnxWxQosStatsBytesOut_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,4),_JnxWxQosStatsBytesOut_Type())
jnxWxQosStatsBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsBytesOut.setStatus(_A)
_JnxWxQosStatsBytesDropped_Type=Counter64
_JnxWxQosStatsBytesDropped_Object=MibTableColumn
jnxWxQosStatsBytesDropped=_JnxWxQosStatsBytesDropped_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,5),_JnxWxQosStatsBytesDropped_Type())
jnxWxQosStatsBytesDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsBytesDropped.setStatus(_A)
_JnxWxQosStatsPktsIn_Type=Counter64
_JnxWxQosStatsPktsIn_Object=MibTableColumn
jnxWxQosStatsPktsIn=_JnxWxQosStatsPktsIn_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,6),_JnxWxQosStatsPktsIn_Type())
jnxWxQosStatsPktsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsPktsIn.setStatus(_A)
_JnxWxQosStatsPktsOut_Type=Counter64
_JnxWxQosStatsPktsOut_Object=MibTableColumn
jnxWxQosStatsPktsOut=_JnxWxQosStatsPktsOut_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,7),_JnxWxQosStatsPktsOut_Type())
jnxWxQosStatsPktsOut.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsPktsOut.setStatus(_A)
_JnxWxQosStatsPktsDropped_Type=Counter64
_JnxWxQosStatsPktsDropped_Object=MibTableColumn
jnxWxQosStatsPktsDropped=_JnxWxQosStatsPktsDropped_Object((1,3,6,1,4,1,8239,2,2,1,2,10,3,1,8),_JnxWxQosStatsPktsDropped_Type())
jnxWxQosStatsPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxQosStatsPktsDropped.setStatus(_A)
_JnxWxStatsQosClassCount_Type=Integer32
_JnxWxStatsQosClassCount_Object=MibScalar
jnxWxStatsQosClassCount=_JnxWxStatsQosClassCount_Object((1,3,6,1,4,1,8239,2,2,1,2,11),_JnxWxStatsQosClassCount_Type())
jnxWxStatsQosClassCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsQosClassCount.setStatus(_A)
_JnxWxStatsQosEndptCount_Type=Integer32
_JnxWxStatsQosEndptCount_Object=MibScalar
jnxWxStatsQosEndptCount=_JnxWxStatsQosEndptCount_Object((1,3,6,1,4,1,8239,2,2,1,2,12),_JnxWxStatsQosEndptCount_Type())
jnxWxStatsQosEndptCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsQosEndptCount.setStatus(_A)
_JnxWxStatsWpEndptCount_Type=Integer32
_JnxWxStatsWpEndptCount_Object=MibScalar
jnxWxStatsWpEndptCount=_JnxWxStatsWpEndptCount_Object((1,3,6,1,4,1,8239,2,2,1,2,13),_JnxWxStatsWpEndptCount_Type())
jnxWxStatsWpEndptCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxStatsWpEndptCount.setStatus(_A)
_JnxWxWanPerf_ObjectIdentity=ObjectIdentity
jnxWxWanPerf=_JnxWxWanPerf_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,2,14))
if mibBuilder.loadTexts:jnxWxWanPerf.setStatus(_A)
_JnxWxWpEndptTable_Object=MibTable
jnxWxWpEndptTable=_JnxWxWpEndptTable_Object((1,3,6,1,4,1,8239,2,2,1,2,14,1))
if mibBuilder.loadTexts:jnxWxWpEndptTable.setStatus(_A)
_JnxWxWpEndptEntry_Object=MibTableRow
jnxWxWpEndptEntry=_JnxWxWpEndptEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,14,1,1))
jnxWxWpEndptEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:jnxWxWpEndptEntry.setStatus(_A)
_JnxWxWpEndptIndex_Type=Integer32
_JnxWxWpEndptIndex_Object=MibTableColumn
jnxWxWpEndptIndex=_JnxWxWpEndptIndex_Object((1,3,6,1,4,1,8239,2,2,1,2,14,1,1,1),_JnxWxWpEndptIndex_Type())
jnxWxWpEndptIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxWxWpEndptIndex.setStatus(_A)
_JnxWxWpEndptIp_Type=IpAddress
_JnxWxWpEndptIp_Object=MibTableColumn
jnxWxWpEndptIp=_JnxWxWpEndptIp_Object((1,3,6,1,4,1,8239,2,2,1,2,14,1,1,2),_JnxWxWpEndptIp_Type())
jnxWxWpEndptIp.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpEndptIp.setStatus(_A)
_JnxWxWpStatsTable_Object=MibTable
jnxWxWpStatsTable=_JnxWxWpStatsTable_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2))
if mibBuilder.loadTexts:jnxWxWpStatsTable.setStatus(_A)
_JnxWxWpStatsEntry_Object=MibTableRow
jnxWxWpStatsEntry=_JnxWxWpStatsEntry_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1))
jnxWxWpStatsEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:jnxWxWpStatsEntry.setStatus(_A)
_JnxWxWpStatsLatencyThresh_Type=Unsigned32
_JnxWxWpStatsLatencyThresh_Object=MibTableColumn
jnxWxWpStatsLatencyThresh=_JnxWxWpStatsLatencyThresh_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,3),_JnxWxWpStatsLatencyThresh_Type())
jnxWxWpStatsLatencyThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLatencyThresh.setStatus(_A)
_JnxWxWpStatsAvgLatency_Type=Unsigned32
_JnxWxWpStatsAvgLatency_Object=MibTableColumn
jnxWxWpStatsAvgLatency=_JnxWxWpStatsAvgLatency_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,4),_JnxWxWpStatsAvgLatency_Type())
jnxWxWpStatsAvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsAvgLatency.setStatus(_A)
_JnxWxWpStatsLatencyCount_Type=Unsigned32
_JnxWxWpStatsLatencyCount_Object=MibTableColumn
jnxWxWpStatsLatencyCount=_JnxWxWpStatsLatencyCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,5),_JnxWxWpStatsLatencyCount_Type())
jnxWxWpStatsLatencyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLatencyCount.setStatus(_A)
_JnxWxWpStatsLatencyAboveThresh_Type=Unsigned32
_JnxWxWpStatsLatencyAboveThresh_Object=MibTableColumn
jnxWxWpStatsLatencyAboveThresh=_JnxWxWpStatsLatencyAboveThresh_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,6),_JnxWxWpStatsLatencyAboveThresh_Type())
jnxWxWpStatsLatencyAboveThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLatencyAboveThresh.setStatus(_A)
_JnxWxWpStatsLatencyAboveThreshCount_Type=Unsigned32
_JnxWxWpStatsLatencyAboveThreshCount_Object=MibTableColumn
jnxWxWpStatsLatencyAboveThreshCount=_JnxWxWpStatsLatencyAboveThreshCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,7),_JnxWxWpStatsLatencyAboveThreshCount_Type())
jnxWxWpStatsLatencyAboveThreshCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLatencyAboveThreshCount.setStatus(_A)
_JnxWxWpStatsLossPercent_Type=Unsigned32
_JnxWxWpStatsLossPercent_Object=MibTableColumn
jnxWxWpStatsLossPercent=_JnxWxWpStatsLossPercent_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,8),_JnxWxWpStatsLossPercent_Type())
jnxWxWpStatsLossPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLossPercent.setStatus(_A)
_JnxWxWpStatsLossCount_Type=Unsigned32
_JnxWxWpStatsLossCount_Object=MibTableColumn
jnxWxWpStatsLossCount=_JnxWxWpStatsLossCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,9),_JnxWxWpStatsLossCount_Type())
jnxWxWpStatsLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLossCount.setStatus(_A)
_JnxWxWpStatsEventCount_Type=Unsigned32
_JnxWxWpStatsEventCount_Object=MibTableColumn
jnxWxWpStatsEventCount=_JnxWxWpStatsEventCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,10),_JnxWxWpStatsEventCount_Type())
jnxWxWpStatsEventCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsEventCount.setStatus(_A)
_JnxWxWpStatsDiversionCount_Type=Unsigned32
_JnxWxWpStatsDiversionCount_Object=MibTableColumn
jnxWxWpStatsDiversionCount=_JnxWxWpStatsDiversionCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,11),_JnxWxWpStatsDiversionCount_Type())
jnxWxWpStatsDiversionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsDiversionCount.setStatus(_A)
_JnxWxWpStatsReturnCount_Type=Unsigned32
_JnxWxWpStatsReturnCount_Object=MibTableColumn
jnxWxWpStatsReturnCount=_JnxWxWpStatsReturnCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,12),_JnxWxWpStatsReturnCount_Type())
jnxWxWpStatsReturnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsReturnCount.setStatus(_A)
_JnxWxWpStatsLastDown_Type=Unsigned32
_JnxWxWpStatsLastDown_Object=MibTableColumn
jnxWxWpStatsLastDown=_JnxWxWpStatsLastDown_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,13),_JnxWxWpStatsLastDown_Type())
jnxWxWpStatsLastDown.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsLastDown.setStatus(_A)
_JnxWxWpStatsUnavailableCount_Type=Unsigned32
_JnxWxWpStatsUnavailableCount_Object=MibTableColumn
jnxWxWpStatsUnavailableCount=_JnxWxWpStatsUnavailableCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,14),_JnxWxWpStatsUnavailableCount_Type())
jnxWxWpStatsUnavailableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsUnavailableCount.setStatus(_A)
_JnxWxWpStatsMinuteCount_Type=Unsigned32
_JnxWxWpStatsMinuteCount_Object=MibTableColumn
jnxWxWpStatsMinuteCount=_JnxWxWpStatsMinuteCount_Object((1,3,6,1,4,1,8239,2,2,1,2,14,2,1,15),_JnxWxWpStatsMinuteCount_Type())
jnxWxWpStatsMinuteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxWxWpStatsMinuteCount.setStatus(_A)
_JnxWxEvents_ObjectIdentity=ObjectIdentity
jnxWxEvents=_JnxWxEvents_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,3))
if mibBuilder.loadTexts:jnxWxEvents.setStatus(_A)
_JnxWxEventObjs_ObjectIdentity=ObjectIdentity
jnxWxEventObjs=_JnxWxEventObjs_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,3,1))
if mibBuilder.loadTexts:jnxWxEventObjs.setStatus(_A)
_JnxWxEventEvents_ObjectIdentity=ObjectIdentity
jnxWxEventEvents=_JnxWxEventEvents_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,3,2))
if mibBuilder.loadTexts:jnxWxEventEvents.setStatus(_A)
_JnxWxEventEventsV2_ObjectIdentity=ObjectIdentity
jnxWxEventEventsV2=_JnxWxEventEventsV2_ObjectIdentity((1,3,6,1,4,1,8239,2,2,1,3,2,0))
if mibBuilder.loadTexts:jnxWxEventEventsV2.setStatus(_A)
jnxWxAsmEntry.registerAugmentions((_E,_N))
jnxWxAsmStatsEntry.setIndexNames(*jnxWxAsmEntry.getIndexNames())
jnxWxAppEntry.registerAugmentions((_E,_O))
jnxWxAppAggrStatsEntry.setIndexNames(*jnxWxAppEntry.getIndexNames())
jnxWxEventRipAuthFailure=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,1))
jnxWxEventRipAuthFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventRipAuthFailure.setStatus(_A)
jnxWxEventCompressionBufferOverflow=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,2))
jnxWxEventCompressionBufferOverflow.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventCompressionBufferOverflow.setStatus(_A)
jnxWxEventCompressionSessionClosed=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,3))
jnxWxEventCompressionSessionClosed.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventCompressionSessionClosed.setStatus(_A)
jnxWxEventDecompressionSessionClosed=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,4))
jnxWxEventDecompressionSessionClosed.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventDecompressionSessionClosed.setStatus(_A)
jnxWxEventCompressionSessionOpened=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,5))
jnxWxEventCompressionSessionOpened.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventCompressionSessionOpened.setStatus(_A)
jnxWxEventDecompressionSessionOpened=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,6))
jnxWxEventDecompressionSessionOpened.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventDecompressionSessionOpened.setStatus(_A)
jnxWxEventPrimaryRegServerUnreachable=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,7))
jnxWxEventPrimaryRegServerUnreachable.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventPrimaryRegServerUnreachable.setStatus(_A)
jnxWxEventSecondaryRegServerUnreachable=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,8))
jnxWxEventSecondaryRegServerUnreachable.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventSecondaryRegServerUnreachable.setStatus(_A)
jnxWxEventMultiNodeMasterUp=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,9))
jnxWxEventMultiNodeMasterUp.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventMultiNodeMasterUp.setStatus(_A)
jnxWxEventMultiNodeMasterDown=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,10))
jnxWxEventMultiNodeMasterDown.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventMultiNodeMasterDown.setStatus(_A)
jnxWxEventMultiNodeLastUp=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,11))
jnxWxEventMultiNodeLastUp.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventMultiNodeLastUp.setStatus(_A)
jnxWxEventMultiNodeLastDown=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,12))
jnxWxEventMultiNodeLastDown.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventMultiNodeLastDown.setStatus(_A)
jnxWxEventPrimaryDownBackupEngaged=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,13))
jnxWxEventPrimaryDownBackupEngaged.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventPrimaryDownBackupEngaged.setStatus(_A)
jnxWxEventPrimaryDownBackupEngageFailed=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,14))
jnxWxEventPrimaryDownBackupEngageFailed.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventPrimaryDownBackupEngageFailed.setStatus(_A)
jnxWxEventPrimaryUpBackupDisengaged=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,15))
jnxWxEventPrimaryUpBackupDisengaged.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventPrimaryUpBackupDisengaged.setStatus(_A)
jnxWxEventMultiPathStatusChange=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,16))
jnxWxEventMultiPathStatusChange.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventMultiPathStatusChange.setStatus(_A)
jnxWxEventDiskFailure=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,17))
jnxWxEventDiskFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventDiskFailure.setStatus(_A)
jnxWxEventWanPerfStatusChange=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,18))
jnxWxEventWanPerfStatusChange.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventWanPerfStatusChange.setStatus(_A)
jnxWxEventDCQAboveHiWatermark=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,19))
jnxWxEventDCQAboveHiWatermark.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventDCQAboveHiWatermark.setStatus(_A)
jnxWxEventDCQBelowHiWatermark=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,20))
jnxWxEventDCQBelowHiWatermark.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventDCQBelowHiWatermark.setStatus(_A)
jnxWxEventPerformanceThreshCrossed=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,21))
jnxWxEventPerformanceThreshCrossed.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventPerformanceThreshCrossed.setStatus(_A)
jnxWxEventClientLinkDown=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,22))
jnxWxEventClientLinkDown.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventClientLinkDown.setStatus(_A)
jnxWxEventClientLinkUp=NotificationType((1,3,6,1,4,1,8239,2,2,1,3,2,0,23))
jnxWxEventClientLinkUp.setObjects((_C,_D))
if mibBuilder.loadTexts:jnxWxEventClientLinkUp.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'jnxWxMibModule':jnxWxMibModule,'jnxWxMib':jnxWxMib,'jnxWxConfMib':jnxWxConfMib,'jnxWxObjs':jnxWxObjs,'jnxWxStatsUpdateTime':jnxWxStatsUpdateTime,'jnxWxStatsAsmCount':jnxWxStatsAsmCount,'jnxWxStatsAppCount':jnxWxStatsAppCount,'jnxWxSysStats':jnxWxSysStats,'jnxWxSysStatsBytesInAe':jnxWxSysStatsBytesInAe,'jnxWxSysStatsBytesOutAe':jnxWxSysStatsBytesOutAe,'jnxWxSysStatsPktsInAe':jnxWxSysStatsPktsInAe,'jnxWxSysStatsPktsOutAe':jnxWxSysStatsPktsOutAe,'jnxWxSysStatsBytesOutOob':jnxWxSysStatsBytesOutOob,'jnxWxSysStatsBytesPtNoAe':jnxWxSysStatsBytesPtNoAe,'jnxWxSysStatsPktsPtNoAe':jnxWxSysStatsPktsPtNoAe,'jnxWxSysStatsBytesPtFilter':jnxWxSysStatsBytesPtFilter,'jnxWxSysStatsPktsPtFilter':jnxWxSysStatsPktsPtFilter,'jnxWxSysStatsBytesOfPt':jnxWxSysStatsBytesOfPt,'jnxWxSysStatsPktsOfPt':jnxWxSysStatsPktsOfPt,'jnxWxSysStatsBytesTpIn':jnxWxSysStatsBytesTpIn,'jnxWxSysStatsPktsTpIn':jnxWxSysStatsPktsTpIn,'jnxWxSysStatsBytesTpOut':jnxWxSysStatsBytesTpOut,'jnxWxSysStatsPktsTpOut':jnxWxSysStatsPktsTpOut,'jnxWxSysStatsBytesTpPt':jnxWxSysStatsBytesTpPt,'jnxWxSysStatsPktsTpPt':jnxWxSysStatsPktsTpPt,'jnxWxSysStatsPeakRdn':jnxWxSysStatsPeakRdn,'jnxWxSysStatsThruputIn':jnxWxSysStatsThruputIn,'jnxWxSysStatsThruputOut':jnxWxSysStatsThruputOut,'jnxWxSysStatsBytesInRe':jnxWxSysStatsBytesInRe,'jnxWxSysStatsBytesOutRe':jnxWxSysStatsBytesOutRe,'jnxWxSysStatsPktsInRe':jnxWxSysStatsPktsInRe,'jnxWxSysStatsPktsOutRe':jnxWxSysStatsPktsOutRe,'jnxWxSysStatsPktSizeIn1':jnxWxSysStatsPktSizeIn1,'jnxWxSysStatsPktSizeIn2':jnxWxSysStatsPktSizeIn2,'jnxWxSysStatsPktSizeIn3':jnxWxSysStatsPktSizeIn3,'jnxWxSysStatsPktSizeIn4':jnxWxSysStatsPktSizeIn4,'jnxWxSysStatsPktSizeIn5':jnxWxSysStatsPktSizeIn5,'jnxWxSysStatsPktSizeIn6':jnxWxSysStatsPktSizeIn6,'jnxWxSysStatsPktSizeOut1':jnxWxSysStatsPktSizeOut1,'jnxWxSysStatsPktSizeOut2':jnxWxSysStatsPktSizeOut2,'jnxWxSysStatsPktSizeOut3':jnxWxSysStatsPktSizeOut3,'jnxWxSysStatsPktSizeOut4':jnxWxSysStatsPktSizeOut4,'jnxWxSysStatsPktSizeOut5':jnxWxSysStatsPktSizeOut5,'jnxWxSysStatsPktSizeOut6':jnxWxSysStatsPktSizeOut6,'jnxWxAsm':jnxWxAsm,'jnxWxAsmTable':jnxWxAsmTable,'jnxWxAsmEntry':jnxWxAsmEntry,_G:jnxWxAsmIndex,'jnxWxAsmIpAddress':jnxWxAsmIpAddress,'jnxWxAsmStatsTable':jnxWxAsmStatsTable,_N:jnxWxAsmStatsEntry,'jnxWxAsmStatsPktsIn':jnxWxAsmStatsPktsIn,'jnxWxAsmStatsPktsOut':jnxWxAsmStatsPktsOut,'jnxWxAsmStatsBytesIn':jnxWxAsmStatsBytesIn,'jnxWxAsmStatsBytesOut':jnxWxAsmStatsBytesOut,'jnxWxVirtEndptTable':jnxWxVirtEndptTable,'jnxWxVirtEndptEntry':jnxWxVirtEndptEntry,_M:jnxWxVirtEndptIndex,'jnxWxVirtEndptName':jnxWxVirtEndptName,'jnxWxVirtEndptSubnetCount':jnxWxVirtEndptSubnetCount,'jnxWxApp':jnxWxApp,'jnxWxAppTable':jnxWxAppTable,'jnxWxAppEntry':jnxWxAppEntry,_H:jnxWxAppIndex,'jnxWxAppAppName':jnxWxAppAppName,'jnxWxAppStatsTable':jnxWxAppStatsTable,'jnxWxAppStatsEntry':jnxWxAppStatsEntry,'jnxWxAppStatsBytesIn':jnxWxAppStatsBytesIn,'jnxWxAppStatsBytesOut':jnxWxAppStatsBytesOut,'jnxWxAppStatsBytesInPercent':jnxWxAppStatsBytesInPercent,'jnxWxAppStatsAppName':jnxWxAppStatsAppName,'jnxWxAppStatsAccelBytesIn':jnxWxAppStatsAccelBytesIn,'jnxWxAppStatsActiveSessionTime':jnxWxAppStatsActiveSessionTime,'jnxWxAppStatsEstBoostBytes':jnxWxAppStatsEstBoostBytes,'jnxWxAppStatsBytesOutWxc':jnxWxAppStatsBytesOutWxc,'jnxWxAppAggrStatsTable':jnxWxAppAggrStatsTable,_O:jnxWxAppAggrStatsEntry,'jnxWxAppAggrStatsBytesInRe':jnxWxAppAggrStatsBytesInRe,'jnxWxAppAggrStatsBytesOutRe':jnxWxAppAggrStatsBytesOutRe,'jnxWxAppAggrStatsBytesInPercent':jnxWxAppAggrStatsBytesInPercent,'jnxWxWanStatsTable':jnxWxWanStatsTable,'jnxWxWanStatsEntry':jnxWxWanStatsEntry,'jnxWxWanStatsBytesToWan':jnxWxWanStatsBytesToWan,'jnxWxWanStatsBytesFromWan':jnxWxWanStatsBytesFromWan,'jnxWxAccelAppNameTable':jnxWxAccelAppNameTable,'jnxWxAccelAppNameEntry':jnxWxAccelAppNameEntry,_I:jnxWxAccelAppIndex,'jnxWxAccelAppName':jnxWxAccelAppName,'jnxWxAccelAppStatsTable':jnxWxAccelAppStatsTable,'jnxWxAccelAppStatsEntry':jnxWxAccelAppStatsEntry,'jnxWxAccelAppTimeWithAccel':jnxWxAccelAppTimeWithAccel,'jnxWxAccelAppTimeWithoutAccel':jnxWxAccelAppTimeWithoutAccel,'jnxWxBurstStats':jnxWxBurstStats,'jnxWxBurstStatsStartTime':jnxWxBurstStatsStartTime,'jnxWxBurstStatsBpsIn':jnxWxBurstStatsBpsIn,'jnxWxBurstStatsBpsOut':jnxWxBurstStatsBpsOut,'jnxWxBurstStatsBpsPt':jnxWxBurstStatsBpsPt,'jnxWxStatsAccelAppCount':jnxWxStatsAccelAppCount,'jnxWxStatsVirtEndptCount':jnxWxStatsVirtEndptCount,'jnxWxQos':jnxWxQos,'jnxWxQosEndptTable':jnxWxQosEndptTable,'jnxWxQosEndptEntry':jnxWxQosEndptEntry,_J:jnxWxQosEndptIndex,'jnxWxQosEndptIdentifier':jnxWxQosEndptIdentifier,'jnxWxQosClassTable':jnxWxQosClassTable,'jnxWxQosClassEntry':jnxWxQosClassEntry,_K:jnxWxQosClassIndex,'jnxWxQosClassName':jnxWxQosClassName,'jnxWxQosStatsTable':jnxWxQosStatsTable,'jnxWxQosStatsEntry':jnxWxQosStatsEntry,'jnxWxQosStatsBytesIn':jnxWxQosStatsBytesIn,'jnxWxQosStatsBytesOut':jnxWxQosStatsBytesOut,'jnxWxQosStatsBytesDropped':jnxWxQosStatsBytesDropped,'jnxWxQosStatsPktsIn':jnxWxQosStatsPktsIn,'jnxWxQosStatsPktsOut':jnxWxQosStatsPktsOut,'jnxWxQosStatsPktsDropped':jnxWxQosStatsPktsDropped,'jnxWxStatsQosClassCount':jnxWxStatsQosClassCount,'jnxWxStatsQosEndptCount':jnxWxStatsQosEndptCount,'jnxWxStatsWpEndptCount':jnxWxStatsWpEndptCount,'jnxWxWanPerf':jnxWxWanPerf,'jnxWxWpEndptTable':jnxWxWpEndptTable,'jnxWxWpEndptEntry':jnxWxWpEndptEntry,_L:jnxWxWpEndptIndex,'jnxWxWpEndptIp':jnxWxWpEndptIp,'jnxWxWpStatsTable':jnxWxWpStatsTable,'jnxWxWpStatsEntry':jnxWxWpStatsEntry,'jnxWxWpStatsLatencyThresh':jnxWxWpStatsLatencyThresh,'jnxWxWpStatsAvgLatency':jnxWxWpStatsAvgLatency,'jnxWxWpStatsLatencyCount':jnxWxWpStatsLatencyCount,'jnxWxWpStatsLatencyAboveThresh':jnxWxWpStatsLatencyAboveThresh,'jnxWxWpStatsLatencyAboveThreshCount':jnxWxWpStatsLatencyAboveThreshCount,'jnxWxWpStatsLossPercent':jnxWxWpStatsLossPercent,'jnxWxWpStatsLossCount':jnxWxWpStatsLossCount,'jnxWxWpStatsEventCount':jnxWxWpStatsEventCount,'jnxWxWpStatsDiversionCount':jnxWxWpStatsDiversionCount,'jnxWxWpStatsReturnCount':jnxWxWpStatsReturnCount,'jnxWxWpStatsLastDown':jnxWxWpStatsLastDown,'jnxWxWpStatsUnavailableCount':jnxWxWpStatsUnavailableCount,'jnxWxWpStatsMinuteCount':jnxWxWpStatsMinuteCount,'jnxWxEvents':jnxWxEvents,'jnxWxEventObjs':jnxWxEventObjs,'jnxWxEventEvents':jnxWxEventEvents,'jnxWxEventEventsV2':jnxWxEventEventsV2,'jnxWxEventRipAuthFailure':jnxWxEventRipAuthFailure,'jnxWxEventCompressionBufferOverflow':jnxWxEventCompressionBufferOverflow,'jnxWxEventCompressionSessionClosed':jnxWxEventCompressionSessionClosed,'jnxWxEventDecompressionSessionClosed':jnxWxEventDecompressionSessionClosed,'jnxWxEventCompressionSessionOpened':jnxWxEventCompressionSessionOpened,'jnxWxEventDecompressionSessionOpened':jnxWxEventDecompressionSessionOpened,'jnxWxEventPrimaryRegServerUnreachable':jnxWxEventPrimaryRegServerUnreachable,'jnxWxEventSecondaryRegServerUnreachable':jnxWxEventSecondaryRegServerUnreachable,'jnxWxEventMultiNodeMasterUp':jnxWxEventMultiNodeMasterUp,'jnxWxEventMultiNodeMasterDown':jnxWxEventMultiNodeMasterDown,'jnxWxEventMultiNodeLastUp':jnxWxEventMultiNodeLastUp,'jnxWxEventMultiNodeLastDown':jnxWxEventMultiNodeLastDown,'jnxWxEventPrimaryDownBackupEngaged':jnxWxEventPrimaryDownBackupEngaged,'jnxWxEventPrimaryDownBackupEngageFailed':jnxWxEventPrimaryDownBackupEngageFailed,'jnxWxEventPrimaryUpBackupDisengaged':jnxWxEventPrimaryUpBackupDisengaged,'jnxWxEventMultiPathStatusChange':jnxWxEventMultiPathStatusChange,'jnxWxEventDiskFailure':jnxWxEventDiskFailure,'jnxWxEventWanPerfStatusChange':jnxWxEventWanPerfStatusChange,'jnxWxEventDCQAboveHiWatermark':jnxWxEventDCQAboveHiWatermark,'jnxWxEventDCQBelowHiWatermark':jnxWxEventDCQBelowHiWatermark,'jnxWxEventPerformanceThreshCrossed':jnxWxEventPerformanceThreshCrossed,'jnxWxEventClientLinkDown':jnxWxEventClientLinkDown,'jnxWxEventClientLinkUp':jnxWxEventClientLinkUp})