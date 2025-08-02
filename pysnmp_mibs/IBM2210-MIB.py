_M='ibmServiceGenericPort'
_L='IBM2210-MIB'
_K='NotificationType'
_J='proElsTrapSubSystem'
_I='proElsTrapSeqs'
_H='proElsTrapEvent'
_G='proElsSubSysEventMsg'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='PROTEON-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
proElsSubSysEventMsg,proElsTrapEvent,proElsTrapSeqs,proElsTrapSubSystem=mibBuilder.importSymbols(_C,_G,_H,_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Proteon_ObjectIdentity=ObjectIdentity
proteon=_Proteon_ObjectIdentity((1,3,6,1,4,1,1))
_ProXfaceGenericTable_Object=MibTable
proXfaceGenericTable=_ProXfaceGenericTable_Object((1,3,6,1,4,1,1,2))
if mibBuilder.loadTexts:proXfaceGenericTable.setStatus(_A)
_ProXfaceGenericEntry_Object=MibTableRow
proXfaceGenericEntry=_ProXfaceGenericEntry_Object((1,3,6,1,4,1,1,2,1))
proXfaceGenericEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:proXfaceGenericEntry.setStatus(_A)
class _ProXfaceGenericType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64)));namedValues=NamedValues(*(('vi',1),('pn10',2),('pn80',3),('chaos',4),('xeth',5),('m1822',6),('scc',7),('ieth',8),('peth',9),('com2',10),('com4',11),('omn',12),('pn4',13),('hyper',14),('wdeth',15),('gwslc',16),('x25',17),('pqsx',18),('atr',19),('fddi',20),('vlane',21),('vcom4',22),('pn16',23),('atcomsl',24),('ceth',25),('csl',26),('seth',27),('srlygwsl',28),('srlyatc2',29),('srlycsl',30),('srbtnl',31),('sdlcrly',32),('nseth',33),('x25atc2',34),('x25csl',35),('x25dcsl',36),('qsl',37),('ydcisdn',38),('tsl',39),('qslch',40),('v25bis',41),('hssi',42),('quiceth',43),('quictkr',44),('quicsl',45),('quicbisdn',46),('vlic',47),('atm',48),('escon',49),('isdnpri',50),('quic4wan',51),('quic8wan',52),('quic4mdm',53),('quic8mdm',54),('pawx21',55),('pawv36',56),('pawrs232',57),('nwescon',58),('atmvirt',59),('appnl',60),('v34',61),('mp',62),('atmpmpls',63),('eth100',64)))
_ProXfaceGenericType_Type.__name__=_D
_ProXfaceGenericType_Object=MibTableColumn
proXfaceGenericType=_ProXfaceGenericType_Object((1,3,6,1,4,1,1,2,1,1),_ProXfaceGenericType_Type())
proXfaceGenericType.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericType.setStatus(_A)
_ProXfaceGenericCSR_Type=Integer32
_ProXfaceGenericCSR_Object=MibTableColumn
proXfaceGenericCSR=_ProXfaceGenericCSR_Object((1,3,6,1,4,1,1,2,1,2),_ProXfaceGenericCSR_Type())
proXfaceGenericCSR.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericCSR.setStatus(_A)
_ProXfaceGenericIntVec_Type=Integer32
_ProXfaceGenericIntVec_Object=MibTableColumn
proXfaceGenericIntVec=_ProXfaceGenericIntVec_Object((1,3,6,1,4,1,1,2,1,3),_ProXfaceGenericIntVec_Type())
proXfaceGenericIntVec.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericIntVec.setStatus(_A)
_ProXfaceGenericMaintInt_Type=Integer32
_ProXfaceGenericMaintInt_Object=MibTableColumn
proXfaceGenericMaintInt=_ProXfaceGenericMaintInt_Object((1,3,6,1,4,1,1,2,1,4),_ProXfaceGenericMaintInt_Type())
proXfaceGenericMaintInt.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericMaintInt.setStatus(_A)
_ProXfaceGenericMaintLim_Type=Integer32
_ProXfaceGenericMaintLim_Object=MibTableColumn
proXfaceGenericMaintLim=_ProXfaceGenericMaintLim_Object((1,3,6,1,4,1,1,2,1,5),_ProXfaceGenericMaintLim_Type())
proXfaceGenericMaintLim.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericMaintLim.setStatus(_A)
_ProXfaceGenericNextTest_Type=Integer32
_ProXfaceGenericNextTest_Object=MibTableColumn
proXfaceGenericNextTest=_ProXfaceGenericNextTest_Object((1,3,6,1,4,1,1,2,1,6),_ProXfaceGenericNextTest_Type())
proXfaceGenericNextTest.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericNextTest.setStatus(_A)
_ProXfaceGenericNextMaint_Type=Integer32
_ProXfaceGenericNextMaint_Object=MibTableColumn
proXfaceGenericNextMaint=_ProXfaceGenericNextMaint_Object((1,3,6,1,4,1,1,2,1,7),_ProXfaceGenericNextMaint_Type())
proXfaceGenericNextMaint.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericNextMaint.setStatus(_A)
_ProXfaceGenericMaintCnt_Type=Counter32
_ProXfaceGenericMaintCnt_Object=MibTableColumn
proXfaceGenericMaintCnt=_ProXfaceGenericMaintCnt_Object((1,3,6,1,4,1,1,2,1,8),_ProXfaceGenericMaintCnt_Type())
proXfaceGenericMaintCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericMaintCnt.setStatus(_A)
_ProXfaceGenericMaintFails_Type=Counter32
_ProXfaceGenericMaintFails_Object=MibTableColumn
proXfaceGenericMaintFails=_ProXfaceGenericMaintFails_Object((1,3,6,1,4,1,1,2,1,9),_ProXfaceGenericMaintFails_Type())
proXfaceGenericMaintFails.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericMaintFails.setStatus(_A)
_ProXfaceGenericTestPasses_Type=Counter32
_ProXfaceGenericTestPasses_Object=MibTableColumn
proXfaceGenericTestPasses=_ProXfaceGenericTestPasses_Object((1,3,6,1,4,1,1,2,1,10),_ProXfaceGenericTestPasses_Type())
proXfaceGenericTestPasses.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericTestPasses.setStatus(_A)
_ProXfaceGenericTestFails_Type=Counter32
_ProXfaceGenericTestFails_Object=MibTableColumn
proXfaceGenericTestFails=_ProXfaceGenericTestFails_Object((1,3,6,1,4,1,1,2,1,11),_ProXfaceGenericTestFails_Type())
proXfaceGenericTestFails.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericTestFails.setStatus(_A)
_ProXfaceGenericModuleId_Type=Integer32
_ProXfaceGenericModuleId_Object=MibTableColumn
proXfaceGenericModuleId=_ProXfaceGenericModuleId_Object((1,3,6,1,4,1,1,2,1,12),_ProXfaceGenericModuleId_Type())
proXfaceGenericModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:proXfaceGenericModuleId.setStatus(_A)
_Proto_ObjectIdentity=ObjectIdentity
proto=_Proto_ObjectIdentity((1,3,6,1,4,1,1,3))
_General_ObjectIdentity=ObjectIdentity
general=_General_ObjectIdentity((1,3,6,1,4,1,1,3,1))
_Proip_ObjectIdentity=ObjectIdentity
proip=_Proip_ObjectIdentity((1,3,6,1,4,1,1,3,2))
_Defgw_ObjectIdentity=ObjectIdentity
defgw=_Defgw_ObjectIdentity((1,3,6,1,4,1,1,3,2,1))
_ProProtoIpDefGwAddress_Type=IpAddress
_ProProtoIpDefGwAddress_Object=MibScalar
proProtoIpDefGwAddress=_ProProtoIpDefGwAddress_Object((1,3,6,1,4,1,1,3,2,1,1),_ProProtoIpDefGwAddress_Type())
proProtoIpDefGwAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:proProtoIpDefGwAddress.setStatus(_A)
_ProProtoIpDefGwCost_Type=Integer32
_ProProtoIpDefGwCost_Object=MibScalar
proProtoIpDefGwCost=_ProProtoIpDefGwCost_Object((1,3,6,1,4,1,1,3,2,1,2),_ProProtoIpDefGwCost_Type())
proProtoIpDefGwCost.setMaxAccess(_B)
if mibBuilder.loadTexts:proProtoIpDefGwCost.setStatus(_A)
_ProProtoIpDefGwAge_Type=Integer32
_ProProtoIpDefGwAge_Object=MibScalar
proProtoIpDefGwAge=_ProProtoIpDefGwAge_Object((1,3,6,1,4,1,1,3,2,1,3),_ProProtoIpDefGwAge_Type())
proProtoIpDefGwAge.setMaxAccess(_B)
if mibBuilder.loadTexts:proProtoIpDefGwAge.setStatus(_A)
_PDot3ChipSets_ObjectIdentity=ObjectIdentity
pDot3ChipSets=_PDot3ChipSets_ObjectIdentity((1,3,6,1,4,1,1,5))
_PDot3ChipMC68EN360_ObjectIdentity=ObjectIdentity
pDot3ChipMC68EN360=_PDot3ChipMC68EN360_ObjectIdentity((1,3,6,1,4,1,1,5,1))
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm2210_ObjectIdentity=ObjectIdentity
ibm2210=_Ibm2210_ObjectIdentity((1,3,6,1,4,1,2,6,72))
_Ibm2210admin_ObjectIdentity=ObjectIdentity
ibm2210admin=_Ibm2210admin_ObjectIdentity((1,3,6,1,4,1,2,6,72,1))
_Ibm2210system_ObjectIdentity=ObjectIdentity
ibm2210system=_Ibm2210system_ObjectIdentity((1,3,6,1,4,1,2,6,72,2))
_Ibm2210hardware_ObjectIdentity=ObjectIdentity
ibm2210hardware=_Ibm2210hardware_ObjectIdentity((1,3,6,1,4,1,2,6,72,3))
_Ibm2210hardwareinfo_ObjectIdentity=ObjectIdentity
ibm2210hardwareinfo=_Ibm2210hardwareinfo_ObjectIdentity((1,3,6,1,4,1,2,6,72,3,1))
_IbmServiceGenericTable_Object=MibTable
ibmServiceGenericTable=_IbmServiceGenericTable_Object((1,3,6,1,4,1,2,6,72,3,1,1))
if mibBuilder.loadTexts:ibmServiceGenericTable.setStatus(_A)
_IbmServiceGenericEntry_Object=MibTableRow
ibmServiceGenericEntry=_IbmServiceGenericEntry_Object((1,3,6,1,4,1,2,6,72,3,1,1,1))
ibmServiceGenericEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:ibmServiceGenericEntry.setStatus(_A)
_IbmServiceGenericPort_Type=Integer32
_IbmServiceGenericPort_Object=MibTableColumn
ibmServiceGenericPort=_IbmServiceGenericPort_Object((1,3,6,1,4,1,2,6,72,3,1,1,1,1),_IbmServiceGenericPort_Type())
ibmServiceGenericPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmServiceGenericPort.setStatus(_A)
_IbmServiceGenericBaurdrate_Type=Integer32
_IbmServiceGenericBaurdrate_Object=MibTableColumn
ibmServiceGenericBaurdrate=_IbmServiceGenericBaurdrate_Object((1,3,6,1,4,1,2,6,72,3,1,1,1,2),_IbmServiceGenericBaurdrate_Type())
ibmServiceGenericBaurdrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmServiceGenericBaurdrate.setStatus(_A)
class _IbmServiceGenericType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eia232',1),('modem',2),('nocard',3)))
_IbmServiceGenericType_Type.__name__=_D
_IbmServiceGenericType_Object=MibTableColumn
ibmServiceGenericType=_IbmServiceGenericType_Object((1,3,6,1,4,1,2,6,72,3,1,1,1,3),_IbmServiceGenericType_Type())
ibmServiceGenericType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmServiceGenericType.setStatus(_A)
_Ibm2210routing_ObjectIdentity=ObjectIdentity
ibm2210routing=_Ibm2210routing_ObjectIdentity((1,3,6,1,4,1,2,6,72,4))
_Ibm2210switching_ObjectIdentity=ObjectIdentity
ibm2210switching=_Ibm2210switching_ObjectIdentity((1,3,6,1,4,1,2,6,72,5))
ibmElsTrapV1=NotificationType((1,3,6,1,4,1,2,6,72,0,1))
ibmElsTrapV1.setObjects(*((_C,_I),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:ibmElsTrapV1.setStatus('')
ibmElsTrapV2=NotificationType((1,3,6,1,4,1,2,6,72,0,2))
ibmElsTrapV2.setObjects((_C,_G))
if mibBuilder.loadTexts:ibmElsTrapV2.setStatus('')
mibBuilder.exportSymbols(_L,**{'proteon':proteon,'proXfaceGenericTable':proXfaceGenericTable,'proXfaceGenericEntry':proXfaceGenericEntry,'proXfaceGenericType':proXfaceGenericType,'proXfaceGenericCSR':proXfaceGenericCSR,'proXfaceGenericIntVec':proXfaceGenericIntVec,'proXfaceGenericMaintInt':proXfaceGenericMaintInt,'proXfaceGenericMaintLim':proXfaceGenericMaintLim,'proXfaceGenericNextTest':proXfaceGenericNextTest,'proXfaceGenericNextMaint':proXfaceGenericNextMaint,'proXfaceGenericMaintCnt':proXfaceGenericMaintCnt,'proXfaceGenericMaintFails':proXfaceGenericMaintFails,'proXfaceGenericTestPasses':proXfaceGenericTestPasses,'proXfaceGenericTestFails':proXfaceGenericTestFails,'proXfaceGenericModuleId':proXfaceGenericModuleId,'proto':proto,'general':general,'proip':proip,'defgw':defgw,'proProtoIpDefGwAddress':proProtoIpDefGwAddress,'proProtoIpDefGwCost':proProtoIpDefGwCost,'proProtoIpDefGwAge':proProtoIpDefGwAge,'pDot3ChipSets':pDot3ChipSets,'pDot3ChipMC68EN360':pDot3ChipMC68EN360,'ibm':ibm,'ibmProd':ibmProd,'ibm2210':ibm2210,'ibmElsTrapV1':ibmElsTrapV1,'ibmElsTrapV2':ibmElsTrapV2,'ibm2210admin':ibm2210admin,'ibm2210system':ibm2210system,'ibm2210hardware':ibm2210hardware,'ibm2210hardwareinfo':ibm2210hardwareinfo,'ibmServiceGenericTable':ibmServiceGenericTable,'ibmServiceGenericEntry':ibmServiceGenericEntry,_M:ibmServiceGenericPort,'ibmServiceGenericBaurdrate':ibmServiceGenericBaurdrate,'ibmServiceGenericType':ibmServiceGenericType,'ibm2210routing':ibm2210routing,'ibm2210switching':ibm2210switching})