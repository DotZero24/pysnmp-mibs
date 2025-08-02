_P='lanSwitchPortIndex'
_O='cpuIndex'
_N='noDaughterBoard'
_M='noBoard'
_L='refused'
_K='boardControllerIndex'
_J='notPlugged'
_I='cabinetIndex'
_H='mCV30-S'
_G='Mega Bytes'
_F='unknown'
_E='OXO-HARDWARE-MIB'
_D='none'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ActivationStatus,PhysicalAddress,oxoMIB=mibBuilder.importSymbols('OXO-MIB','ActivationStatus','PhysicalAddress','oxoMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
oxoHardwareMIB=ModuleIdentity((1,3,6,1,4,1,6486,64,4200,1,1))
if mibBuilder.loadTexts:oxoHardwareMIB.setRevisions(('2015-03-20 14:24',))
class TypeDaughterBoard2Type(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,18,19,20,34,35,36)));namedValues=NamedValues(*((_D,0),('xMEM',1),('vOIP4',2),('vOIP8',3),('vOIP16',4),('mCV30-P',5),(_H,6),('xMEM-1',7),('vOIP4-1',18),('vOIP8-1',19),('vOIP16-1',20),('vOIP4-2',34),('vOIP8-2',35),('vOIP16-2',36)))
_CabinetTable_Object=MibTable
cabinetTable=_CabinetTable_Object((1,3,6,1,4,1,6486,64,4200,1,1,1))
if mibBuilder.loadTexts:cabinetTable.setStatus(_A)
_CabinetEntry_Object=MibTableRow
cabinetEntry=_CabinetEntry_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1))
cabinetEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:cabinetEntry.setStatus(_A)
_CabinetIndex_Type=Integer32
_CabinetIndex_Object=MibTableColumn
cabinetIndex=_CabinetIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,1),_CabinetIndex_Type())
cabinetIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cabinetIndex.setStatus(_A)
class _CabinetRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('master',0),('slave1',1),('slave2',2)))
_CabinetRole_Type.__name__=_C
_CabinetRole_Object=MibTableColumn
cabinetRole=_CabinetRole_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,2),_CabinetRole_Type())
cabinetRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cabinetRole.setStatus(_A)
class _CabinetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_F,0),('rack-1',4),('rack-2',5),('rack-3',6),('rack-1-2G',7),('rack-2-2G',8),('rack-3-2G',9),('rack-XS',10),('rack-XS-N',11),('rack-OTOC-M-2-1G',12),('rack-OTOC-M-2-2G',13),('rack-OTOC-S-2-2G',14)))
_CabinetType_Type.__name__=_C
_CabinetType_Object=MibTableColumn
cabinetType=_CabinetType_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,3),_CabinetType_Type())
cabinetType.setMaxAccess(_B)
if mibBuilder.loadTexts:cabinetType.setStatus(_A)
class _CabinetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_J,0),('notOperational',2),('operational',3)))
_CabinetStatus_Type.__name__=_C
_CabinetStatus_Object=MibTableColumn
cabinetStatus=_CabinetStatus_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,4),_CabinetStatus_Type())
cabinetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cabinetStatus.setStatus(_A)
class _PowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6,7,8,9)));namedValues=NamedValues(*(('ps-Rack-1',4),('ps-Rack-2',5),('ps-Rack-3',6),('ps-Rack-1-2G',7),('ps-Rack-2-2G',8),('ps-Rack-3-2G',9)))
_PowerSupplyType_Type.__name__=_C
_PowerSupplyType_Object=MibTableColumn
powerSupplyType=_PowerSupplyType_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,5),_PowerSupplyType_Type())
powerSupplyType.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyType.setStatus(_A)
class _PowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('main-power-supply',0),('battery',1),(_F,2)))
_PowerSupplyStatus_Type.__name__=_C
_PowerSupplyStatus_Object=MibTableColumn
powerSupplyStatus=_PowerSupplyStatus_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,6),_PowerSupplyStatus_Type())
powerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyStatus.setStatus(_A)
_Fan1Status_Type=ActivationStatus
_Fan1Status_Object=MibTableColumn
fan1Status=_Fan1Status_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,7),_Fan1Status_Type())
fan1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:fan1Status.setStatus(_A)
_Fan2Status_Type=ActivationStatus
_Fan2Status_Object=MibTableColumn
fan2Status=_Fan2Status_Object((1,3,6,1,4,1,6486,64,4200,1,1,1,1,8),_Fan2Status_Type())
fan2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:fan2Status.setStatus(_A)
_BoardTable_Object=MibTable
boardTable=_BoardTable_Object((1,3,6,1,4,1,6486,64,4200,1,1,2))
if mibBuilder.loadTexts:boardTable.setStatus(_A)
_BoardEntry_Object=MibTableRow
boardEntry=_BoardEntry_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1))
boardEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:boardEntry.setStatus(_A)
_BoardControllerIndex_Type=Integer32
_BoardControllerIndex_Object=MibTableColumn
boardControllerIndex=_BoardControllerIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,1),_BoardControllerIndex_Type())
boardControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boardControllerIndex.setStatus(_A)
_BoardCpuIndex_Type=Integer32
_BoardCpuIndex_Object=MibTableColumn
boardCpuIndex=_BoardCpuIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,2),_BoardCpuIndex_Type())
boardCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boardCpuIndex.setStatus(_A)
_BoardLanIndex_Type=Integer32
_BoardLanIndex_Object=MibTableColumn
boardLanIndex=_BoardLanIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,3),_BoardLanIndex_Type())
boardLanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boardLanIndex.setStatus(_A)
_BoardDescr_Type=DisplayString
_BoardDescr_Object=MibTableColumn
boardDescr=_BoardDescr_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,4),_BoardDescr_Type())
boardDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:boardDescr.setStatus(_A)
_BoardAccesses_Type=Integer32
_BoardAccesses_Object=MibTableColumn
boardAccesses=_BoardAccesses_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,5),_BoardAccesses_Type())
boardAccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:boardAccesses.setStatus(_A)
class _BoardPresence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('absent',0),('present',1),(_L,3)))
_BoardPresence_Type.__name__=_C
_BoardPresence_Object=MibTableColumn
boardPresence=_BoardPresence_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,6),_BoardPresence_Type())
boardPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPresence.setStatus(_A)
class _BoardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('accepted',1),(_L,2),('initializing',3)))
_BoardStatus_Type.__name__=_C
_BoardStatus_Object=MibTableColumn
boardStatus=_BoardStatus_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,7),_BoardStatus_Type())
boardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardStatus.setStatus(_A)
class _BoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,149,150,151,152,153,154,155,158,159,160,161,162,163,164,165,166,167,168,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,253)));namedValues=NamedValues(*((_M,0),('bRA-DLT0',149),('aTA',150),('aTL',151),('aTL2',152),('aTL4',153),('aC15',154),('dDI',155),('sLI',158),('sLI-1',159),('uAI',160),('pRA',161),('pRA-DLT2',162),('pRA-T1',163),('pRA-DASS2',164),('pCM',165),('aUX',166),('xRA',167),('virtualVoIP',168),('cPU',176),('mIX',177),('bRA',178),('lANX',179),('aPA',180),('t1-CAS',181),('lANX16-1',182),('uAI16-1',183),('bOOST-board',184),('sLI-1-LH',185),('sLI-1-ST',186),('virtual-M-T',187),('lANX-2',188),('mIX-1-L',189),('mIX-1-ST',190),('aMIX-1-L',191),('aMIX-1-ST',192),('sLI-2',193),('mIX-2',194),('bRA-2',195),(_F,253)))
_BoardType_Type.__name__=_C
_BoardType_Object=MibTableColumn
boardType=_BoardType_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,8),_BoardType_Type())
boardType.setMaxAccess(_B)
if mibBuilder.loadTexts:boardType.setStatus(_A)
class _BoardSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,254)));namedValues=NamedValues(*(('mIX048',0),('mIX044',1),('mIX084',2),('mIX248',3),('mIX244',4),('mIX284',5),('mIX448',6),('mIX444',7),('mIX484',8),('mINIMIX',9),('mIXERROR',10),(_F,254)))
_BoardSubType_Type.__name__=_C
_BoardSubType_Object=MibTableColumn
boardSubType=_BoardSubType_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,9),_BoardSubType_Type())
boardSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:boardSubType.setStatus(_A)
class _DaughterBoard1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,14,24,34,44,240,241)));namedValues=NamedValues(*(('mET12K',4),('mET16K',14),('mETCLI',24),('cLINL',34),('cLIUK',44),(_N,240),('gSCLI',241)))
_DaughterBoard1_Type.__name__=_C
_DaughterBoard1_Object=MibTableColumn
daughterBoard1=_DaughterBoard1_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,10),_DaughterBoard1_Type())
daughterBoard1.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard1.setStatus(_A)
class _DaughterBoard2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(240,242)));namedValues=NamedValues(*((_N,240),('cLI',242)))
_DaughterBoard2_Type.__name__=_C
_DaughterBoard2_Object=MibTableColumn
daughterBoard2=_DaughterBoard2_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,11),_DaughterBoard2_Type())
daughterBoard2.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2.setStatus(_A)
class _BoardExternalfeeding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,254)));namedValues=NamedValues(*((_J,0),('powerOK',1),('powerKO',2),('powerOFF',3),(_F,254)))
_BoardExternalfeeding_Type.__name__=_C
_BoardExternalfeeding_Object=MibTableColumn
boardExternalfeeding=_BoardExternalfeeding_Object((1,3,6,1,4,1,6486,64,4200,1,1,2,1,12),_BoardExternalfeeding_Type())
boardExternalfeeding.setMaxAccess(_B)
if mibBuilder.loadTexts:boardExternalfeeding.setStatus(_A)
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,6486,64,4200,1,1,3))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuEntry_Object=MibTableRow
cpuEntry=_CpuEntry_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1))
cpuEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:cpuEntry.setStatus(_A)
_CpuIndex_Type=Integer32
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,1),_CpuIndex_Type())
cpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
class _CpuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('cpu-Aspen-100',0),('cpu-Aspen-133',1),('cpu-PIII',2),('standart-CPU-1',3),('standart-CPU-2',4),('cpu-PIII2',5),('standart-CPU-3',6),('standart-CPU-3M',7),('cpu-PIII3',8),('pOWER-CPU',9),('standart-CPU-4',10),('pOWER-CPU-EE',11)))
_CpuType_Type.__name__=_C
_CpuType_Object=MibTableColumn
cpuType=_CpuType_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,2),_CpuType_Type())
cpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuType.setStatus(_A)
class _CpuRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('call-Handling',0),('voIP',1),('internetAccess',2),('iSDN-RAS',3),(_D,4)))
_CpuRole_Type.__name__=_C
_CpuRole_Object=MibTableColumn
cpuRole=_CpuRole_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,3),_CpuRole_Type())
cpuRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuRole.setStatus(_A)
_CpuSerialNumber_Type=DisplayString
_CpuSerialNumber_Object=MibTableColumn
cpuSerialNumber=_CpuSerialNumber_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,4),_CpuSerialNumber_Type())
cpuSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuSerialNumber.setStatus(_A)
_CpuSoftVersion_Type=DisplayString
_CpuSoftVersion_Object=MibTableColumn
cpuSoftVersion=_CpuSoftVersion_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,5),_CpuSoftVersion_Type())
cpuSoftVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuSoftVersion.setStatus(_A)
_CpuRamSize_Type=Integer32
_CpuRamSize_Object=MibTableColumn
cpuRamSize=_CpuRamSize_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,6),_CpuRamSize_Type())
cpuRamSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuRamSize.setStatus(_A)
if mibBuilder.loadTexts:cpuRamSize.setUnits(_G)
_CpuFlashSize_Type=Integer32
_CpuFlashSize_Object=MibTableColumn
cpuFlashSize=_CpuFlashSize_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,7),_CpuFlashSize_Type())
cpuFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuFlashSize.setStatus(_A)
if mibBuilder.loadTexts:cpuFlashSize.setUnits(_G)
class _DaughterBoard1Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_D,0),('fOR-DPS',1),('wAN',2),('wAN2',3),(_H,4),('dATA-T1',5),('armada-VoiP-DSP',6)))
_DaughterBoard1Type_Type.__name__=_C
_DaughterBoard1Type_Object=MibTableColumn
daughterBoard1Type=_DaughterBoard1Type_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,8),_DaughterBoard1Type_Type())
daughterBoard1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard1Type.setStatus(_A)
_DaughterBoard2Type_Type=TypeDaughterBoard2Type
_DaughterBoard2Type_Object=MibTableColumn
daughterBoard2Type=_DaughterBoard2Type_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,9),_DaughterBoard2Type_Type())
daughterBoard2Type.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2Type.setStatus(_A)
_DaughterBoard2Type2_Type=TypeDaughterBoard2Type
_DaughterBoard2Type2_Object=MibTableColumn
daughterBoard2Type2=_DaughterBoard2Type2_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,10),_DaughterBoard2Type2_Type())
daughterBoard2Type2.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2Type2.setStatus(_A)
class _DaughterBoard3Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('aFU',1)))
_DaughterBoard3Type_Type.__name__=_C
_DaughterBoard3Type_Object=MibTableColumn
daughterBoard3Type=_DaughterBoard3Type_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,11),_DaughterBoard3Type_Type())
daughterBoard3Type.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard3Type.setStatus(_A)
class _DaughterBoard4Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('hSL1',1),('hSL2',2),('sLANX4',3),('miniMIX',4)))
_DaughterBoard4Type_Type.__name__=_C
_DaughterBoard4Type_Object=MibTableColumn
daughterBoard4Type=_DaughterBoard4Type_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,12),_DaughterBoard4Type_Type())
daughterBoard4Type.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard4Type.setStatus(_A)
_DaughterBoard2HDManufacturer_Type=DisplayString
_DaughterBoard2HDManufacturer_Object=MibTableColumn
daughterBoard2HDManufacturer=_DaughterBoard2HDManufacturer_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,13),_DaughterBoard2HDManufacturer_Type())
daughterBoard2HDManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2HDManufacturer.setStatus(_A)
_DaughterBoard2HDSize_Type=Integer32
_DaughterBoard2HDSize_Object=MibTableColumn
daughterBoard2HDSize=_DaughterBoard2HDSize_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,14),_DaughterBoard2HDSize_Type())
daughterBoard2HDSize.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2HDSize.setStatus(_A)
if mibBuilder.loadTexts:daughterBoard2HDSize.setUnits(_G)
_DaughterBoard2FlashSize_Type=Integer32
_DaughterBoard2FlashSize_Object=MibTableColumn
daughterBoard2FlashSize=_DaughterBoard2FlashSize_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,15),_DaughterBoard2FlashSize_Type())
daughterBoard2FlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:daughterBoard2FlashSize.setStatus(_A)
if mibBuilder.loadTexts:daughterBoard2FlashSize.setUnits(_G)
class _MotherVoipPresence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,256,257)));namedValues=NamedValues(*(('no-DSP',0),('one-DSP',256),('two-DSP',257)))
_MotherVoipPresence_Type.__name__=_C
_MotherVoipPresence_Object=MibTableColumn
motherVoipPresence=_MotherVoipPresence_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,16),_MotherVoipPresence_Type())
motherVoipPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:motherVoipPresence.setStatus(_A)
_MacAddress_Type=MacAddress
_MacAddress_Object=MibTableColumn
macAddress=_MacAddress_Object((1,3,6,1,4,1,6486,64,4200,1,1,3,1,17),_MacAddress_Type())
macAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
_LanSwitchPortTable_Object=MibTable
lanSwitchPortTable=_LanSwitchPortTable_Object((1,3,6,1,4,1,6486,64,4200,1,1,4))
if mibBuilder.loadTexts:lanSwitchPortTable.setStatus(_A)
_LanSwitchPortEntry_Object=MibTableRow
lanSwitchPortEntry=_LanSwitchPortEntry_Object((1,3,6,1,4,1,6486,64,4200,1,1,4,1))
lanSwitchPortEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:lanSwitchPortEntry.setStatus(_A)
_LanSwitchPortIndex_Type=PhysicalAddress
_LanSwitchPortIndex_Object=MibTableColumn
lanSwitchPortIndex=_LanSwitchPortIndex_Object((1,3,6,1,4,1,6486,64,4200,1,1,4,1,1),_LanSwitchPortIndex_Type())
lanSwitchPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lanSwitchPortIndex.setStatus(_A)
_LanSwitchPortStatus_Type=Integer32
_LanSwitchPortStatus_Object=MibTableColumn
lanSwitchPortStatus=_LanSwitchPortStatus_Object((1,3,6,1,4,1,6486,64,4200,1,1,4,1,2),_LanSwitchPortStatus_Type())
lanSwitchPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanSwitchPortStatus.setStatus(_A)
_LanSwitchPortMode_Type=Integer32
_LanSwitchPortMode_Object=MibTableColumn
lanSwitchPortMode=_LanSwitchPortMode_Object((1,3,6,1,4,1,6486,64,4200,1,1,4,1,3),_LanSwitchPortMode_Type())
lanSwitchPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lanSwitchPortMode.setStatus(_A)
_LanSwitchPortBase_Type=Integer32
_LanSwitchPortBase_Object=MibTableColumn
lanSwitchPortBase=_LanSwitchPortBase_Object((1,3,6,1,4,1,6486,64,4200,1,1,4,1,4),_LanSwitchPortBase_Type())
lanSwitchPortBase.setMaxAccess(_B)
if mibBuilder.loadTexts:lanSwitchPortBase.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'TypeDaughterBoard2Type':TypeDaughterBoard2Type,'oxoHardwareMIB':oxoHardwareMIB,'cabinetTable':cabinetTable,'cabinetEntry':cabinetEntry,_I:cabinetIndex,'cabinetRole':cabinetRole,'cabinetType':cabinetType,'cabinetStatus':cabinetStatus,'powerSupplyType':powerSupplyType,'powerSupplyStatus':powerSupplyStatus,'fan1Status':fan1Status,'fan2Status':fan2Status,'boardTable':boardTable,'boardEntry':boardEntry,_K:boardControllerIndex,'boardCpuIndex':boardCpuIndex,'boardLanIndex':boardLanIndex,'boardDescr':boardDescr,'boardAccesses':boardAccesses,'boardPresence':boardPresence,'boardStatus':boardStatus,'boardType':boardType,'boardSubType':boardSubType,'daughterBoard1':daughterBoard1,'daughterBoard2':daughterBoard2,'boardExternalfeeding':boardExternalfeeding,'cpuTable':cpuTable,'cpuEntry':cpuEntry,_O:cpuIndex,'cpuType':cpuType,'cpuRole':cpuRole,'cpuSerialNumber':cpuSerialNumber,'cpuSoftVersion':cpuSoftVersion,'cpuRamSize':cpuRamSize,'cpuFlashSize':cpuFlashSize,'daughterBoard1Type':daughterBoard1Type,'daughterBoard2Type':daughterBoard2Type,'daughterBoard2Type2':daughterBoard2Type2,'daughterBoard3Type':daughterBoard3Type,'daughterBoard4Type':daughterBoard4Type,'daughterBoard2HDManufacturer':daughterBoard2HDManufacturer,'daughterBoard2HDSize':daughterBoard2HDSize,'daughterBoard2FlashSize':daughterBoard2FlashSize,'motherVoipPresence':motherVoipPresence,'macAddress':macAddress,'lanSwitchPortTable':lanSwitchPortTable,'lanSwitchPortEntry':lanSwitchPortEntry,_P:lanSwitchPortIndex,'lanSwitchPortStatus':lanSwitchPortStatus,'lanSwitchPortMode':lanSwitchPortMode,'lanSwitchPortBase':lanSwitchPortBase})