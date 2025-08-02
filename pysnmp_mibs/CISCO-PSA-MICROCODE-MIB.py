_S='ciscoPsaMicrocodeNotifGroup'
_R='ciscoPsaMicrocodeParamsGroup'
_Q='ciscoPsaMicrocodeReload'
_P='cpmcNotifEnables'
_O='cpmcBundleFeatures'
_N='cpmcBundleId'
_M='serverCard'
_L='TruthValue'
_K='entPhysicalName'
_J='entPhysicalIndex'
_I='entPhysicalDescr'
_H='cpmcModulePsaFeaturesDisabled'
_G='cpmcModulePsaFeaturesEnabled'
_F='cpmcModulePsaPrevBundleId'
_E='cpmcModulePsaCurrBundleId'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-PSA-MICROCODE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalDescr,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_D,_I,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
ciscoPsaMicrocodeMIB=ModuleIdentity((1,3,6,1,4,1,9,9,259))
if mibBuilder.loadTexts:ciscoPsaMicrocodeMIB.setRevisions(('2002-06-18 00:00',))
class PsaMicrocodeBundleId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('unknown',1),('none',2),('vanillaPOS',3),('vanillaGE',4),('vanillaInuit',5),('vanillaTaz',6),('pircPOS',7),('pircGE',8),('uRPFPOS',9),('vrfSelectionPOS',10),('bgppaPOS',11),('bgppaGE',12),('ipColorPOS',13),('inputAcl128POS',14),('inputAcl128GE',15),('outputAcl128POS',16),('outputAcl128GE',17),('inputAcl448POS',18),('inputAcl448GE',19),('outputAcl448POS',20),('outputAcl448GE',21),(_M,22),('eoMplsGE',23),('frtpPOS',24),('outputAclATM',25),('inputAcl128Taz',26),('vrfSelectionGE',27),('uRPFGE',28),('cscGE',29),('linkBundleSMPOS',30),('linkBundleDMPOS',31),('linkBundleSMGE',32),('linkBundleDMGE',33)))
class PsaMicrocodeFeatures(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('basicIpForwarding',0),('basicMplsSwitching',1),('frameRelaySwitching',2),('eAFrSwitching',3),('frtp',4),('pirc',5),('vrfSelection',6),('uRPF',7),('inputAcl128',8),('outputAcl128',9),('inputAcl448',10),('outputAcl448',11),('sampledNetflow',12),('ipMarking',13),('bgppa',14),('uti',15),('mplsVpn',16),('eoMpls',17),('atmoMpls',18),('csc',19),('multicast',20),('perPacketLoadBalancing',21),('sourceMacAccounting',22),('frSubVrf',23),(_M,24),('mplsSNF',25),('linkBundle',26),('atomDisposition',27)))
_CiscoPsaMicrocodeMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPsaMicrocodeMIBNotifs=_CiscoPsaMicrocodeMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,259,0))
_CiscoPsaMicrocodeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPsaMicrocodeMIBObjects=_CiscoPsaMicrocodeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,259,1))
_CpmcModulePsa_ObjectIdentity=ObjectIdentity
cpmcModulePsa=_CpmcModulePsa_ObjectIdentity((1,3,6,1,4,1,9,9,259,1,1))
_CpmcModulePsaTable_Object=MibTable
cpmcModulePsaTable=_CpmcModulePsaTable_Object((1,3,6,1,4,1,9,9,259,1,1,1))
if mibBuilder.loadTexts:cpmcModulePsaTable.setStatus(_A)
_CpmcModulePsaEntry_Object=MibTableRow
cpmcModulePsaEntry=_CpmcModulePsaEntry_Object((1,3,6,1,4,1,9,9,259,1,1,1,1))
cpmcModulePsaEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cpmcModulePsaEntry.setStatus(_A)
_CpmcModulePsaCurrBundleId_Type=PsaMicrocodeBundleId
_CpmcModulePsaCurrBundleId_Object=MibTableColumn
cpmcModulePsaCurrBundleId=_CpmcModulePsaCurrBundleId_Object((1,3,6,1,4,1,9,9,259,1,1,1,1,1),_CpmcModulePsaCurrBundleId_Type())
cpmcModulePsaCurrBundleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmcModulePsaCurrBundleId.setStatus(_A)
_CpmcModulePsaPrevBundleId_Type=PsaMicrocodeBundleId
_CpmcModulePsaPrevBundleId_Object=MibTableColumn
cpmcModulePsaPrevBundleId=_CpmcModulePsaPrevBundleId_Object((1,3,6,1,4,1,9,9,259,1,1,1,1,2),_CpmcModulePsaPrevBundleId_Type())
cpmcModulePsaPrevBundleId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmcModulePsaPrevBundleId.setStatus(_A)
_CpmcModulePsaFeaturesEnabled_Type=PsaMicrocodeFeatures
_CpmcModulePsaFeaturesEnabled_Object=MibTableColumn
cpmcModulePsaFeaturesEnabled=_CpmcModulePsaFeaturesEnabled_Object((1,3,6,1,4,1,9,9,259,1,1,1,1,3),_CpmcModulePsaFeaturesEnabled_Type())
cpmcModulePsaFeaturesEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmcModulePsaFeaturesEnabled.setStatus(_A)
_CpmcModulePsaFeaturesDisabled_Type=PsaMicrocodeFeatures
_CpmcModulePsaFeaturesDisabled_Object=MibTableColumn
cpmcModulePsaFeaturesDisabled=_CpmcModulePsaFeaturesDisabled_Object((1,3,6,1,4,1,9,9,259,1,1,1,1,4),_CpmcModulePsaFeaturesDisabled_Type())
cpmcModulePsaFeaturesDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmcModulePsaFeaturesDisabled.setStatus(_A)
_CpmcBundle_ObjectIdentity=ObjectIdentity
cpmcBundle=_CpmcBundle_ObjectIdentity((1,3,6,1,4,1,9,9,259,1,2))
_CpmcBundleTable_Object=MibTable
cpmcBundleTable=_CpmcBundleTable_Object((1,3,6,1,4,1,9,9,259,1,2,1))
if mibBuilder.loadTexts:cpmcBundleTable.setStatus(_A)
_CpmcBundleEntry_Object=MibTableRow
cpmcBundleEntry=_CpmcBundleEntry_Object((1,3,6,1,4,1,9,9,259,1,2,1,1))
cpmcBundleEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cpmcBundleEntry.setStatus(_A)
_CpmcBundleId_Type=PsaMicrocodeBundleId
_CpmcBundleId_Object=MibTableColumn
cpmcBundleId=_CpmcBundleId_Object((1,3,6,1,4,1,9,9,259,1,2,1,1,1),_CpmcBundleId_Type())
cpmcBundleId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpmcBundleId.setStatus(_A)
_CpmcBundleFeatures_Type=PsaMicrocodeFeatures
_CpmcBundleFeatures_Object=MibTableColumn
cpmcBundleFeatures=_CpmcBundleFeatures_Object((1,3,6,1,4,1,9,9,259,1,2,1,1,2),_CpmcBundleFeatures_Type())
cpmcBundleFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmcBundleFeatures.setStatus(_A)
_CpmcNotif_ObjectIdentity=ObjectIdentity
cpmcNotif=_CpmcNotif_ObjectIdentity((1,3,6,1,4,1,9,9,259,1,3))
class _CpmcNotifEnables_Type(TruthValue):defaultValue=2
_CpmcNotifEnables_Type.__name__=_L
_CpmcNotifEnables_Object=MibScalar
cpmcNotifEnables=_CpmcNotifEnables_Object((1,3,6,1,4,1,9,9,259,1,3,1),_CpmcNotifEnables_Type())
cpmcNotifEnables.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpmcNotifEnables.setStatus(_A)
_CiscoPsaMicrocodeMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPsaMicrocodeMIBConformance=_CiscoPsaMicrocodeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,259,2))
_CiscoPsaMicrocodeMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPsaMicrocodeMIBCompliances=_CiscoPsaMicrocodeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,259,2,1))
_CiscoPsaMicrocodeMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPsaMicrocodeMIBGroups=_CiscoPsaMicrocodeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,259,2,2))
ciscoPsaMicrocodeParamsGroup=ObjectGroup((1,3,6,1,4,1,9,9,259,2,2,1))
ciscoPsaMicrocodeParamsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoPsaMicrocodeParamsGroup.setStatus(_A)
ciscoPsaMicrocodeReload=NotificationType((1,3,6,1,4,1,9,9,259,0,1))
ciscoPsaMicrocodeReload.setObjects(*((_D,_K),(_D,_I),(_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:ciscoPsaMicrocodeReload.setStatus(_A)
ciscoPsaMicrocodeNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,259,2,2,2))
ciscoPsaMicrocodeNotifGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ciscoPsaMicrocodeNotifGroup.setStatus(_A)
ciscoPsaMicrocodeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,259,2,1,1))
ciscoPsaMicrocodeMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoPsaMicrocodeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PsaMicrocodeBundleId':PsaMicrocodeBundleId,'PsaMicrocodeFeatures':PsaMicrocodeFeatures,'ciscoPsaMicrocodeMIB':ciscoPsaMicrocodeMIB,'ciscoPsaMicrocodeMIBNotifs':ciscoPsaMicrocodeMIBNotifs,_Q:ciscoPsaMicrocodeReload,'ciscoPsaMicrocodeMIBObjects':ciscoPsaMicrocodeMIBObjects,'cpmcModulePsa':cpmcModulePsa,'cpmcModulePsaTable':cpmcModulePsaTable,'cpmcModulePsaEntry':cpmcModulePsaEntry,_E:cpmcModulePsaCurrBundleId,_F:cpmcModulePsaPrevBundleId,_G:cpmcModulePsaFeaturesEnabled,_H:cpmcModulePsaFeaturesDisabled,'cpmcBundle':cpmcBundle,'cpmcBundleTable':cpmcBundleTable,'cpmcBundleEntry':cpmcBundleEntry,_N:cpmcBundleId,_O:cpmcBundleFeatures,'cpmcNotif':cpmcNotif,_P:cpmcNotifEnables,'ciscoPsaMicrocodeMIBConformance':ciscoPsaMicrocodeMIBConformance,'ciscoPsaMicrocodeMIBCompliances':ciscoPsaMicrocodeMIBCompliances,'ciscoPsaMicrocodeMIBCompliance':ciscoPsaMicrocodeMIBCompliance,'ciscoPsaMicrocodeMIBGroups':ciscoPsaMicrocodeMIBGroups,_R:ciscoPsaMicrocodeParamsGroup,_S:ciscoPsaMicrocodeNotifGroup})