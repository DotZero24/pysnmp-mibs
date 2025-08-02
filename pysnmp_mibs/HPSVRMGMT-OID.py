_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpEmbeddedServerMgt=ModuleIdentity((1,3,6,1,4,1,11,5,7))
if mibBuilder.loadTexts:hpEmbeddedServerMgt.setRevisions(('2007-07-09 00:00','2010-04-15 00:00','2012-01-18 00:00','2012-09-14 00:00','2013-03-08 00:00','2013-09-26 00:00','2017-06-19 00:00'))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_HpSysMgt_ObjectIdentity=ObjectIdentity
hpSysMgt=_HpSysMgt_ObjectIdentity((1,3,6,1,4,1,11,5))
_HpChassisMgmtProc_ObjectIdentity=ObjectIdentity
hpChassisMgmtProc=_HpChassisMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,1))
_HpBladeMgmtCard_ObjectIdentity=ObjectIdentity
hpBladeMgmtCard=_HpBladeMgmtCard_ObjectIdentity((1,3,6,1,4,1,11,5,7,1,1))
if mibBuilder.loadTexts:hpBladeMgmtCard.setStatus(_A)
_HpOnboardAdministrator_ObjectIdentity=ObjectIdentity
hpOnboardAdministrator=_HpOnboardAdministrator_ObjectIdentity((1,3,6,1,4,1,11,5,7,1,2))
if mibBuilder.loadTexts:hpOnboardAdministrator.setStatus(_A)
_HpBladeMgmtProc_ObjectIdentity=ObjectIdentity
hpBladeMgmtProc=_HpBladeMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,2))
_HpBHMgmtProc_ObjectIdentity=ObjectIdentity
hpBHMgmtProc=_HpBHMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,2,1))
if mibBuilder.loadTexts:hpBHMgmtProc.setStatus(_A)
_HpServerMgmtProc_ObjectIdentity=ObjectIdentity
hpServerMgmtProc=_HpServerMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,3))
_HpServerGSP_ObjectIdentity=ObjectIdentity
hpServerGSP=_HpServerGSP_ObjectIdentity((1,3,6,1,4,1,11,5,7,3,1))
if mibBuilder.loadTexts:hpServerGSP.setStatus(_A)
_HpServerMP_ObjectIdentity=ObjectIdentity
hpServerMP=_HpServerMP_ObjectIdentity((1,3,6,1,4,1,11,5,7,3,2))
if mibBuilder.loadTexts:hpServerMP.setStatus(_A)
_HpServeriLO3_ObjectIdentity=ObjectIdentity
hpServeriLO3=_HpServeriLO3_ObjectIdentity((1,3,6,1,4,1,11,5,7,3,3))
if mibBuilder.loadTexts:hpServeriLO3.setStatus(_A)
_HpPartitionSvrMgmtProc_ObjectIdentity=ObjectIdentity
hpPartitionSvrMgmtProc=_HpPartitionSvrMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,4))
_HpHiMPartGSP_ObjectIdentity=ObjectIdentity
hpHiMPartGSP=_HpHiMPartGSP_ObjectIdentity((1,3,6,1,4,1,11,5,7,4,1))
if mibBuilder.loadTexts:hpHiMPartGSP.setStatus(_A)
_HpMidMPartMP_ObjectIdentity=ObjectIdentity
hpMidMPartMP=_HpMidMPartMP_ObjectIdentity((1,3,6,1,4,1,11,5,7,4,2))
if mibBuilder.loadTexts:hpMidMPartMP.setStatus(_A)
_HpHiMPartArchMP_ObjectIdentity=ObjectIdentity
hpHiMPartArchMP=_HpHiMPartArchMP_ObjectIdentity((1,3,6,1,4,1,11,5,7,4,3))
if mibBuilder.loadTexts:hpHiMPartArchMP.setStatus(_A)
_HpMidMPartArchMP_ObjectIdentity=ObjectIdentity
hpMidMPartArchMP=_HpMidMPartArchMP_ObjectIdentity((1,3,6,1,4,1,11,5,7,4,4))
if mibBuilder.loadTexts:hpMidMPartArchMP.setStatus(_A)
_HpModuleMgmtProc_ObjectIdentity=ObjectIdentity
hpModuleMgmtProc=_HpModuleMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,5))
_HpVCEthernetModule_ObjectIdentity=ObjectIdentity
hpVCEthernetModule=_HpVCEthernetModule_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,1))
if mibBuilder.loadTexts:hpVCEthernetModule.setStatus(_A)
_HpVCModuleIsVC24PortCmdr_ObjectIdentity=ObjectIdentity
hpVCModuleIsVC24PortCmdr=_HpVCModuleIsVC24PortCmdr_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,3))
if mibBuilder.loadTexts:hpVCModuleIsVC24PortCmdr.setStatus(_A)
_HpVCFlex_10_10D_Module_ObjectIdentity=ObjectIdentity
hpVCFlex_10_10D_Module=_HpVCFlex_10_10D_Module_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,4))
if mibBuilder.loadTexts:hpVCFlex_10_10D_Module.setStatus(_A)
_HpVCFlexFabric_20_40_F8_Module_ObjectIdentity=ObjectIdentity
hpVCFlexFabric_20_40_F8_Module=_HpVCFlexFabric_20_40_F8_Module_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,6))
if mibBuilder.loadTexts:hpVCFlexFabric_20_40_F8_Module.setStatus(_A)
_HpHyperscaleFabric_ObjectIdentity=ObjectIdentity
hpHyperscaleFabric=_HpHyperscaleFabric_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,7))
if mibBuilder.loadTexts:hpHyperscaleFabric.setStatus(_A)
_HpMoonshot_45G_Switch_Module_ObjectIdentity=ObjectIdentity
hpMoonshot_45G_Switch_Module=_HpMoonshot_45G_Switch_Module_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,7,1))
if mibBuilder.loadTexts:hpMoonshot_45G_Switch_Module.setStatus(_A)
_HpVCSE_40Gb_F8_Module_ObjectIdentity=ObjectIdentity
hpVCSE_40Gb_F8_Module=_HpVCSE_40Gb_F8_Module_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8))
if mibBuilder.loadTexts:hpVCSE_40Gb_F8_Module.setStatus(_A)
_HpVCSE_100Gb_F32_Module_ObjectIdentity=ObjectIdentity
hpVCSE_100Gb_F32_Module=_HpVCSE_100Gb_F32_Module_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9))
if mibBuilder.loadTexts:hpVCSE_100Gb_F32_Module.setStatus(_A)
mibBuilder.exportSymbols('HPSVRMGMT-OID',**{'hp':hp,'hpSysMgt':hpSysMgt,'hpEmbeddedServerMgt':hpEmbeddedServerMgt,'hpChassisMgmtProc':hpChassisMgmtProc,'hpBladeMgmtCard':hpBladeMgmtCard,'hpOnboardAdministrator':hpOnboardAdministrator,'hpBladeMgmtProc':hpBladeMgmtProc,'hpBHMgmtProc':hpBHMgmtProc,'hpServerMgmtProc':hpServerMgmtProc,'hpServerGSP':hpServerGSP,'hpServerMP':hpServerMP,'hpServeriLO3':hpServeriLO3,'hpPartitionSvrMgmtProc':hpPartitionSvrMgmtProc,'hpHiMPartGSP':hpHiMPartGSP,'hpMidMPartMP':hpMidMPartMP,'hpHiMPartArchMP':hpHiMPartArchMP,'hpMidMPartArchMP':hpMidMPartArchMP,'hpModuleMgmtProc':hpModuleMgmtProc,'hpVCEthernetModule':hpVCEthernetModule,'hpVCModuleIsVC24PortCmdr':hpVCModuleIsVC24PortCmdr,'hpVCFlex-10-10D-Module':hpVCFlex_10_10D_Module,'hpVCFlexFabric-20-40-F8-Module':hpVCFlexFabric_20_40_F8_Module,'hpHyperscaleFabric':hpHyperscaleFabric,'hpMoonshot-45G-Switch-Module':hpMoonshot_45G_Switch_Module,'hpVCSE-40Gb-F8-Module':hpVCSE_40Gb_F8_Module,'hpVCSE-100Gb-F32-Module':hpVCSE_100Gb_F32_Module})