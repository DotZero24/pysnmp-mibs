_i='0.1 percent'
_h='0.01 dmt symbols'
_g='sixteenDMTSymbols'
_f='fifteenDMTSymbols'
_e='fourteenDMTSymbols'
_d='thirteenDMTSymbols'
_c='twelveDMTSymbols'
_b='elevenDMTSymbols'
_a='tenDMTSymbols'
_Z='nineDMTSymbols'
_Y='eightDMTSymbols'
_X='sevenDMTSymbols'
_W='sixDMTSymbols'
_V='fiveDMTSymbols'
_U='fourDMTSymbols'
_T='threeDMTSymbols'
_S='obsolete'
_R='g9925AnxM'
_Q='adsl1MultiMode'
_P='readsl'
_O='SnmpAdminString'
_N='adslLineConfProfileName'
_M='ADSL-LINE-MIB'
_L='disable'
_K='twoDMTSymbols'
_J='oneDMTSymbols'
_I='halfDMTSymbols'
_H='zeroDMTSymbols'
_G='OctetString'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineConfProfileName,=mibBuilder.importSymbols(_M,_N)
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols(_E,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adTAOctAdslID=ModuleIdentity((1,3,6,1,4,1,664,6,432))
_AdTAOctAdsl_ObjectIdentity=ObjectIdentity
adTAOctAdsl=_AdTAOctAdsl_ObjectIdentity((1,3,6,1,4,1,664,1,432))
_AdTAOctAdslalarms_ObjectIdentity=ObjectIdentity
adTAOctAdslalarms=_AdTAOctAdslalarms_ObjectIdentity((1,3,6,1,4,1,664,1,432,101))
_AdTAOctAdslwPOTS_ObjectIdentity=ObjectIdentity
adTAOctAdslwPOTS=_AdTAOctAdslwPOTS_ObjectIdentity((1,3,6,1,4,1,664,1,455))
_AdTA5k32pADSL2_ObjectIdentity=ObjectIdentity
adTA5k32pADSL2=_AdTA5k32pADSL2_ObjectIdentity((1,3,6,1,4,1,664,1,752))
_AdTA5k24pPOTSADSL2_ObjectIdentity=ObjectIdentity
adTA5k24pPOTSADSL2=_AdTA5k24pPOTSADSL2_ObjectIdentity((1,3,6,1,4,1,664,1,858))
_AdTA5k32pADSL2int_ObjectIdentity=ObjectIdentity
adTA5k32pADSL2int=_AdTA5k32pADSL2int_ObjectIdentity((1,3,6,1,4,1,664,1,1043))
_AdTAOctAdslmg_ObjectIdentity=ObjectIdentity
adTAOctAdslmg=_AdTAOctAdslmg_ObjectIdentity((1,3,6,1,4,1,664,2,432))
_AdTAOctAdslProv_ObjectIdentity=ObjectIdentity
adTAOctAdslProv=_AdTAOctAdslProv_ObjectIdentity((1,3,6,1,4,1,664,2,432,1))
_AdTAOctAdslProv2_ObjectIdentity=ObjectIdentity
adTAOctAdslProv2=_AdTAOctAdslProv2_ObjectIdentity((1,3,6,1,4,1,664,2,432,2))
_AdTAOctAdslConfProfileExtTable_Object=MibTable
adTAOctAdslConfProfileExtTable=_AdTAOctAdslConfProfileExtTable_Object((1,3,6,1,4,1,664,2,432,2,1))
if mibBuilder.loadTexts:adTAOctAdslConfProfileExtTable.setStatus(_A)
_AdTAOctAdslConfProfileExtEntry_Object=MibTableRow
adTAOctAdslConfProfileExtEntry=_AdTAOctAdslConfProfileExtEntry_Object((1,3,6,1,4,1,664,2,432,2,1,1))
adTAOctAdslConfProfileExtEntry.setIndexNames((1,_M,_N))
if mibBuilder.loadTexts:adTAOctAdslConfProfileExtEntry.setStatus(_A)
class _AdTAOctAdslConfProfileLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noChannel',1),('fastOnly',2),('interleavedOnly',3),('fastOrInterleaved',4),('fastAndInterleaved',5)))
_AdTAOctAdslConfProfileLineType_Type.__name__=_C
_AdTAOctAdslConfProfileLineType_Object=MibTableColumn
adTAOctAdslConfProfileLineType=_AdTAOctAdslConfProfileLineType_Object((1,3,6,1,4,1,664,2,432,2,1,1,1),_AdTAOctAdslConfProfileLineType_Type())
adTAOctAdslConfProfileLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslConfProfileLineType.setStatus(_A)
class _AdTAOctAdslConfProfileServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('multiMode',1),('t1413',2),('gDMT',3),('gLite',4),('g9923',5),('g9924',6),('g9925',7),(_P,8),(_Q,9),(_R,10)))
_AdTAOctAdslConfProfileServiceMode_Type.__name__=_C
_AdTAOctAdslConfProfileServiceMode_Object=MibTableColumn
adTAOctAdslConfProfileServiceMode=_AdTAOctAdslConfProfileServiceMode_Object((1,3,6,1,4,1,664,2,432,2,1,1,2),_AdTAOctAdslConfProfileServiceMode_Type())
adTAOctAdslConfProfileServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslConfProfileServiceMode.setStatus(_A)
class _AdTAOctAdslConfProfileIndexApplied_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdTAOctAdslConfProfileIndexApplied_Type.__name__=_C
_AdTAOctAdslConfProfileIndexApplied_Object=MibTableColumn
adTAOctAdslConfProfileIndexApplied=_AdTAOctAdslConfProfileIndexApplied_Object((1,3,6,1,4,1,664,2,432,2,1,1,3),_AdTAOctAdslConfProfileIndexApplied_Type())
adTAOctAdslConfProfileIndexApplied.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslConfProfileIndexApplied.setStatus(_A)
class _AdTAOctAdslConfProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdTAOctAdslConfProfileName_Type.__name__=_O
_AdTAOctAdslConfProfileName_Object=MibTableColumn
adTAOctAdslConfProfileName=_AdTAOctAdslConfProfileName_Object((1,3,6,1,4,1,664,2,432,2,1,1,4),_AdTAOctAdslConfProfileName_Type())
adTAOctAdslConfProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslConfProfileName.setStatus(_A)
class _AdTAOctAdslAtucConfProfileInterleaveMinINP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4)))
_AdTAOctAdslAtucConfProfileInterleaveMinINP_Type.__name__=_C
_AdTAOctAdslAtucConfProfileInterleaveMinINP_Object=MibTableColumn
adTAOctAdslAtucConfProfileInterleaveMinINP=_AdTAOctAdslAtucConfProfileInterleaveMinINP_Object((1,3,6,1,4,1,664,2,432,2,1,1,5),_AdTAOctAdslAtucConfProfileInterleaveMinINP_Type())
adTAOctAdslAtucConfProfileInterleaveMinINP.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslAtucConfProfileInterleaveMinINP.setStatus(_S)
class _AdTAOctAdslAturConfProfileInterleaveMinINP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4)))
_AdTAOctAdslAturConfProfileInterleaveMinINP_Type.__name__=_C
_AdTAOctAdslAturConfProfileInterleaveMinINP_Object=MibTableColumn
adTAOctAdslAturConfProfileInterleaveMinINP=_AdTAOctAdslAturConfProfileInterleaveMinINP_Object((1,3,6,1,4,1,664,2,432,2,1,1,6),_AdTAOctAdslAturConfProfileInterleaveMinINP_Type())
adTAOctAdslAturConfProfileInterleaveMinINP.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturConfProfileInterleaveMinINP.setStatus(_S)
if mibBuilder.loadTexts:adTAOctAdslAturConfProfileInterleaveMinINP.setUnits('0.5 DMT symbols')
class _AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_c,14),(_d,15),(_e,16),(_f,17),(_g,18)))
_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type.__name__=_C
_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Object=MibTableColumn
adTAOctAdslAtucConfProfileInterleaveMinInpRev2=_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Object((1,3,6,1,4,1,664,2,432,2,1,1,7),_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type())
adTAOctAdslAtucConfProfileInterleaveMinInpRev2.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslAtucConfProfileInterleaveMinInpRev2.setStatus(_A)
class _AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_c,14),(_d,15),(_e,16),(_f,17),(_g,18)))
_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type.__name__=_C
_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Object=MibTableColumn
adTAOctAdslAturConfProfileInterleaveMinInpRev2=_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Object((1,3,6,1,4,1,664,2,432,2,1,1,8),_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type())
adTAOctAdslAturConfProfileInterleaveMinInpRev2.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslAturConfProfileInterleaveMinInpRev2.setStatus(_A)
_AdTAOctAdslConfLineTable_Object=MibTable
adTAOctAdslConfLineTable=_AdTAOctAdslConfLineTable_Object((1,3,6,1,4,1,664,2,432,2,2))
if mibBuilder.loadTexts:adTAOctAdslConfLineTable.setStatus(_A)
_AdTAOctAdslConfLineEntry_Object=MibTableRow
adTAOctAdslConfLineEntry=_AdTAOctAdslConfLineEntry_Object((1,3,6,1,4,1,664,2,432,2,2,1))
adTAOctAdslConfLineEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslConfLineEntry.setStatus(_A)
class _AdTAOctAdslHamBandMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_L,2)))
_AdTAOctAdslHamBandMask_Type.__name__=_C
_AdTAOctAdslHamBandMask_Object=MibTableColumn
adTAOctAdslHamBandMask=_AdTAOctAdslHamBandMask_Object((1,3,6,1,4,1,664,2,432,2,2,1,1),_AdTAOctAdslHamBandMask_Type())
adTAOctAdslHamBandMask.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslHamBandMask.setStatus(_A)
class _AdTAOctAdslCabinetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('enableTone110',2),('enableTone130',3),('enableTone250',4)))
_AdTAOctAdslCabinetMode_Type.__name__=_C
_AdTAOctAdslCabinetMode_Object=MibTableColumn
adTAOctAdslCabinetMode=_AdTAOctAdslCabinetMode_Object((1,3,6,1,4,1,664,2,432,2,2,1,2),_AdTAOctAdslCabinetMode_Type())
adTAOctAdslCabinetMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslCabinetMode.setStatus(_A)
class _AdTAOctAdslPowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('dBm10',2),('dBm12',3),('dBm14',4)))
_AdTAOctAdslPowerThreshold_Type.__name__=_C
_AdTAOctAdslPowerThreshold_Object=MibTableColumn
adTAOctAdslPowerThreshold=_AdTAOctAdslPowerThreshold_Object((1,3,6,1,4,1,664,2,432,2,2,1,3),_AdTAOctAdslPowerThreshold_Type())
adTAOctAdslPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslPowerThreshold.setStatus(_A)
_AdTAOctAdslAtucCarrierMask_Type=OctetString
_AdTAOctAdslAtucCarrierMask_Object=MibTableColumn
adTAOctAdslAtucCarrierMask=_AdTAOctAdslAtucCarrierMask_Object((1,3,6,1,4,1,664,2,432,2,2,1,4),_AdTAOctAdslAtucCarrierMask_Type())
adTAOctAdslAtucCarrierMask.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslAtucCarrierMask.setStatus(_A)
_AdTAOctAdslAturCarrierMask_Type=OctetString
_AdTAOctAdslAturCarrierMask_Object=MibTableColumn
adTAOctAdslAturCarrierMask=_AdTAOctAdslAturCarrierMask_Object((1,3,6,1,4,1,664,2,432,2,2,1,5),_AdTAOctAdslAturCarrierMask_Type())
adTAOctAdslAturCarrierMask.setMaxAccess(_D)
if mibBuilder.loadTexts:adTAOctAdslAturCarrierMask.setStatus(_A)
_AdTAOctAdslStatus2_ObjectIdentity=ObjectIdentity
adTAOctAdslStatus2=_AdTAOctAdslStatus2_ObjectIdentity((1,3,6,1,4,1,664,2,432,4))
_AdTAOctAdslLineTable_Object=MibTable
adTAOctAdslLineTable=_AdTAOctAdslLineTable_Object((1,3,6,1,4,1,664,2,432,4,1))
if mibBuilder.loadTexts:adTAOctAdslLineTable.setStatus(_A)
_AdTAOctAdslLineEntry_Object=MibTableRow
adTAOctAdslLineEntry=_AdTAOctAdslLineEntry_Object((1,3,6,1,4,1,664,2,432,4,1,1))
adTAOctAdslLineEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslLineEntry.setStatus(_A)
class _AdTAOctAdslCurrLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('training',4)))
_AdTAOctAdslCurrLinkStatus_Type.__name__=_C
_AdTAOctAdslCurrLinkStatus_Object=MibTableColumn
adTAOctAdslCurrLinkStatus=_AdTAOctAdslCurrLinkStatus_Object((1,3,6,1,4,1,664,2,432,4,1,1,1),_AdTAOctAdslCurrLinkStatus_Type())
adTAOctAdslCurrLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslCurrLinkStatus.setStatus(_A)
class _AdTAOctAdslCurrStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('reserved',1),('t1413',2),('gDMT',3),('gLite',4),('g9923',5),('g9924',6),('g9925',7),(_P,8),(_Q,9),(_R,10)))
_AdTAOctAdslCurrStandard_Type.__name__=_C
_AdTAOctAdslCurrStandard_Object=MibTableColumn
adTAOctAdslCurrStandard=_AdTAOctAdslCurrStandard_Object((1,3,6,1,4,1,664,2,432,4,1,1,2),_AdTAOctAdslCurrStandard_Type())
adTAOctAdslCurrStandard.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslCurrStandard.setStatus(_A)
class _AdTAOctAdslBitAllocationMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AdTAOctAdslBitAllocationMap_Type.__name__=_G
_AdTAOctAdslBitAllocationMap_Object=MibTableColumn
adTAOctAdslBitAllocationMap=_AdTAOctAdslBitAllocationMap_Object((1,3,6,1,4,1,664,2,432,4,1,1,3),_AdTAOctAdslBitAllocationMap_Type())
adTAOctAdslBitAllocationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslBitAllocationMap.setStatus(_A)
class _AdTAOctAdslBitAllocationMapGroup2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AdTAOctAdslBitAllocationMapGroup2_Type.__name__=_G
_AdTAOctAdslBitAllocationMapGroup2_Object=MibTableColumn
adTAOctAdslBitAllocationMapGroup2=_AdTAOctAdslBitAllocationMapGroup2_Object((1,3,6,1,4,1,664,2,432,4,1,1,4),_AdTAOctAdslBitAllocationMapGroup2_Type())
adTAOctAdslBitAllocationMapGroup2.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslBitAllocationMapGroup2.setStatus(_A)
class _AdTAOctAdslUsSnrMarginMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_AdTAOctAdslUsSnrMarginMap_Type.__name__=_G
_AdTAOctAdslUsSnrMarginMap_Object=MibTableColumn
adTAOctAdslUsSnrMarginMap=_AdTAOctAdslUsSnrMarginMap_Object((1,3,6,1,4,1,664,2,432,4,1,1,5),_AdTAOctAdslUsSnrMarginMap_Type())
adTAOctAdslUsSnrMarginMap.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslUsSnrMarginMap.setStatus(_A)
if mibBuilder.loadTexts:adTAOctAdslUsSnrMarginMap.setUnits('0.1 dB')
_AdTAOctAdslAtucPhysTable_Object=MibTable
adTAOctAdslAtucPhysTable=_AdTAOctAdslAtucPhysTable_Object((1,3,6,1,4,1,664,2,432,4,2))
if mibBuilder.loadTexts:adTAOctAdslAtucPhysTable.setStatus(_A)
_AdTAOctAdslAtucPhysEntry_Object=MibTableRow
adTAOctAdslAtucPhysEntry=_AdTAOctAdslAtucPhysEntry_Object((1,3,6,1,4,1,664,2,432,4,2,1))
adTAOctAdslAtucPhysEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAtucPhysEntry.setStatus(_A)
_AdTAOctAdslAtucNumParityBytes_Type=Integer32
_AdTAOctAdslAtucNumParityBytes_Object=MibTableColumn
adTAOctAdslAtucNumParityBytes=_AdTAOctAdslAtucNumParityBytes_Object((1,3,6,1,4,1,664,2,432,4,2,1,2),_AdTAOctAdslAtucNumParityBytes_Type())
adTAOctAdslAtucNumParityBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtucNumParityBytes.setStatus(_A)
_AdTAOctAdslAtucFramesPerCodeword_Type=Integer32
_AdTAOctAdslAtucFramesPerCodeword_Object=MibTableColumn
adTAOctAdslAtucFramesPerCodeword=_AdTAOctAdslAtucFramesPerCodeword_Object((1,3,6,1,4,1,664,2,432,4,2,1,3),_AdTAOctAdslAtucFramesPerCodeword_Type())
adTAOctAdslAtucFramesPerCodeword.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtucFramesPerCodeword.setStatus(_A)
_AdTAOctAdslAtucInterleavingDepth_Type=Integer32
_AdTAOctAdslAtucInterleavingDepth_Object=MibTableColumn
adTAOctAdslAtucInterleavingDepth=_AdTAOctAdslAtucInterleavingDepth_Object((1,3,6,1,4,1,664,2,432,4,2,1,4),_AdTAOctAdslAtucInterleavingDepth_Type())
adTAOctAdslAtucInterleavingDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtucInterleavingDepth.setStatus(_A)
_AdTAOctAdslAturPhysTable_Object=MibTable
adTAOctAdslAturPhysTable=_AdTAOctAdslAturPhysTable_Object((1,3,6,1,4,1,664,2,432,4,3))
if mibBuilder.loadTexts:adTAOctAdslAturPhysTable.setStatus(_A)
_AdTAOctAdslAturPhysEntry_Object=MibTableRow
adTAOctAdslAturPhysEntry=_AdTAOctAdslAturPhysEntry_Object((1,3,6,1,4,1,664,2,432,4,3,1))
adTAOctAdslAturPhysEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAturPhysEntry.setStatus(_A)
_AdTAOctAdslAturNumParityBytes_Type=Integer32
_AdTAOctAdslAturNumParityBytes_Object=MibTableColumn
adTAOctAdslAturNumParityBytes=_AdTAOctAdslAturNumParityBytes_Object((1,3,6,1,4,1,664,2,432,4,3,1,2),_AdTAOctAdslAturNumParityBytes_Type())
adTAOctAdslAturNumParityBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturNumParityBytes.setStatus(_A)
_AdTAOctAdslAturFramesPerCodeword_Type=Integer32
_AdTAOctAdslAturFramesPerCodeword_Object=MibTableColumn
adTAOctAdslAturFramesPerCodeword=_AdTAOctAdslAturFramesPerCodeword_Object((1,3,6,1,4,1,664,2,432,4,3,1,3),_AdTAOctAdslAturFramesPerCodeword_Type())
adTAOctAdslAturFramesPerCodeword.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturFramesPerCodeword.setStatus(_A)
_AdTAOctAdslAturInterleavingDepth_Type=Integer32
_AdTAOctAdslAturInterleavingDepth_Object=MibTableColumn
adTAOctAdslAturInterleavingDepth=_AdTAOctAdslAturInterleavingDepth_Object((1,3,6,1,4,1,664,2,432,4,3,1,4),_AdTAOctAdslAturInterleavingDepth_Type())
adTAOctAdslAturInterleavingDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturInterleavingDepth.setStatus(_A)
class _AdTAOctAdslAturCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048575))
_AdTAOctAdslAturCapabilities_Type.__name__=_C
_AdTAOctAdslAturCapabilities_Object=MibTableColumn
adTAOctAdslAturCapabilities=_AdTAOctAdslAturCapabilities_Object((1,3,6,1,4,1,664,2,432,4,3,1,5),_AdTAOctAdslAturCapabilities_Type())
adTAOctAdslAturCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturCapabilities.setStatus(_A)
_AdTAOctAdslAturInvProviderCode_Type=SnmpAdminString
_AdTAOctAdslAturInvProviderCode_Object=MibTableColumn
adTAOctAdslAturInvProviderCode=_AdTAOctAdslAturInvProviderCode_Object((1,3,6,1,4,1,664,2,432,4,3,1,6),_AdTAOctAdslAturInvProviderCode_Type())
adTAOctAdslAturInvProviderCode.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturInvProviderCode.setStatus(_A)
_AdTAOctAdslAtucChanTable_Object=MibTable
adTAOctAdslAtucChanTable=_AdTAOctAdslAtucChanTable_Object((1,3,6,1,4,1,664,2,432,4,4))
if mibBuilder.loadTexts:adTAOctAdslAtucChanTable.setStatus(_A)
_AdTAOctAdslAtucChanEntry_Object=MibTableRow
adTAOctAdslAtucChanEntry=_AdTAOctAdslAtucChanEntry_Object((1,3,6,1,4,1,664,2,432,4,4,1))
adTAOctAdslAtucChanEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAtucChanEntry.setStatus(_A)
_AdTAOctAdslAtucChanINP_Type=Gauge32
_AdTAOctAdslAtucChanINP_Object=MibTableColumn
adTAOctAdslAtucChanINP=_AdTAOctAdslAtucChanINP_Object((1,3,6,1,4,1,664,2,432,4,4,1,1),_AdTAOctAdslAtucChanINP_Type())
adTAOctAdslAtucChanINP.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtucChanINP.setStatus(_A)
if mibBuilder.loadTexts:adTAOctAdslAtucChanINP.setUnits(_h)
_AdTAOctAdslAtucRelativeCap_Type=Gauge32
_AdTAOctAdslAtucRelativeCap_Object=MibTableColumn
adTAOctAdslAtucRelativeCap=_AdTAOctAdslAtucRelativeCap_Object((1,3,6,1,4,1,664,2,432,4,4,1,2),_AdTAOctAdslAtucRelativeCap_Type())
adTAOctAdslAtucRelativeCap.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtucRelativeCap.setStatus(_A)
if mibBuilder.loadTexts:adTAOctAdslAtucRelativeCap.setUnits(_i)
_AdTAOctAdslAturChanTable_Object=MibTable
adTAOctAdslAturChanTable=_AdTAOctAdslAturChanTable_Object((1,3,6,1,4,1,664,2,432,4,5))
if mibBuilder.loadTexts:adTAOctAdslAturChanTable.setStatus(_A)
_AdTAOctAdslAturChanEntry_Object=MibTableRow
adTAOctAdslAturChanEntry=_AdTAOctAdslAturChanEntry_Object((1,3,6,1,4,1,664,2,432,4,5,1))
adTAOctAdslAturChanEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAturChanEntry.setStatus(_A)
_AdTAOctAdslAturChanINP_Type=Gauge32
_AdTAOctAdslAturChanINP_Object=MibTableColumn
adTAOctAdslAturChanINP=_AdTAOctAdslAturChanINP_Object((1,3,6,1,4,1,664,2,432,4,5,1,1),_AdTAOctAdslAturChanINP_Type())
adTAOctAdslAturChanINP.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturChanINP.setStatus(_A)
if mibBuilder.loadTexts:adTAOctAdslAturChanINP.setUnits(_h)
_AdTAOctAdslAturRelativeCap_Type=Gauge32
_AdTAOctAdslAturRelativeCap_Object=MibTableColumn
adTAOctAdslAturRelativeCap=_AdTAOctAdslAturRelativeCap_Object((1,3,6,1,4,1,664,2,432,4,5,1,2),_AdTAOctAdslAturRelativeCap_Type())
adTAOctAdslAturRelativeCap.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAturRelativeCap.setStatus(_A)
if mibBuilder.loadTexts:adTAOctAdslAturRelativeCap.setUnits(_i)
_AdTAOctAdslAtmAtucCellCountTable_Object=MibTable
adTAOctAdslAtmAtucCellCountTable=_AdTAOctAdslAtmAtucCellCountTable_Object((1,3,6,1,4,1,664,2,432,4,6))
if mibBuilder.loadTexts:adTAOctAdslAtmAtucCellCountTable.setStatus(_A)
_AdTAOctAdslAtmAtucCellCountEntry_Object=MibTableRow
adTAOctAdslAtmAtucCellCountEntry=_AdTAOctAdslAtmAtucCellCountEntry_Object((1,3,6,1,4,1,664,2,432,4,6,1))
adTAOctAdslAtmAtucCellCountEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAtmAtucCellCountEntry.setStatus(_A)
_AdTAOctAdslAtmAtucCellCount_Type=Unsigned32
_AdTAOctAdslAtmAtucCellCount_Object=MibTableColumn
adTAOctAdslAtmAtucCellCount=_AdTAOctAdslAtmAtucCellCount_Object((1,3,6,1,4,1,664,2,432,4,6,1,1),_AdTAOctAdslAtmAtucCellCount_Type())
adTAOctAdslAtmAtucCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtmAtucCellCount.setStatus(_A)
_AdTAOctAdslAtmAtucIdleCellCount_Type=Unsigned32
_AdTAOctAdslAtmAtucIdleCellCount_Object=MibTableColumn
adTAOctAdslAtmAtucIdleCellCount=_AdTAOctAdslAtmAtucIdleCellCount_Object((1,3,6,1,4,1,664,2,432,4,6,1,2),_AdTAOctAdslAtmAtucIdleCellCount_Type())
adTAOctAdslAtmAtucIdleCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtmAtucIdleCellCount.setStatus(_A)
_AdTAOctAdslAtmAtucHecErrorCount_Type=Unsigned32
_AdTAOctAdslAtmAtucHecErrorCount_Object=MibTableColumn
adTAOctAdslAtmAtucHecErrorCount=_AdTAOctAdslAtmAtucHecErrorCount_Object((1,3,6,1,4,1,664,2,432,4,6,1,3),_AdTAOctAdslAtmAtucHecErrorCount_Type())
adTAOctAdslAtmAtucHecErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtmAtucHecErrorCount.setStatus(_A)
_AdTAOctAdslAtmAturCellCountTable_Object=MibTable
adTAOctAdslAtmAturCellCountTable=_AdTAOctAdslAtmAturCellCountTable_Object((1,3,6,1,4,1,664,2,432,4,7))
if mibBuilder.loadTexts:adTAOctAdslAtmAturCellCountTable.setStatus(_A)
_AdTAOctAdslAtmAturCellCountEntry_Object=MibTableRow
adTAOctAdslAtmAturCellCountEntry=_AdTAOctAdslAtmAturCellCountEntry_Object((1,3,6,1,4,1,664,2,432,4,7,1))
adTAOctAdslAtmAturCellCountEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adTAOctAdslAtmAturCellCountEntry.setStatus(_A)
_AdTAOctAdslAtmAturCellCount_Type=Unsigned32
_AdTAOctAdslAtmAturCellCount_Object=MibTableColumn
adTAOctAdslAtmAturCellCount=_AdTAOctAdslAtmAturCellCount_Object((1,3,6,1,4,1,664,2,432,4,7,1,1),_AdTAOctAdslAtmAturCellCount_Type())
adTAOctAdslAtmAturCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtmAturCellCount.setStatus(_A)
_AdTAOctAdslAtmAturIdleCellCount_Type=Unsigned32
_AdTAOctAdslAtmAturIdleCellCount_Object=MibTableColumn
adTAOctAdslAtmAturIdleCellCount=_AdTAOctAdslAtmAturIdleCellCount_Object((1,3,6,1,4,1,664,2,432,4,7,1,2),_AdTAOctAdslAtmAturIdleCellCount_Type())
adTAOctAdslAtmAturIdleCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adTAOctAdslAtmAturIdleCellCount.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TAOCTADSL2-MIB',**{'adTAOctAdsl':adTAOctAdsl,'adTAOctAdslalarms':adTAOctAdslalarms,'adTAOctAdslwPOTS':adTAOctAdslwPOTS,'adTA5k32pADSL2':adTA5k32pADSL2,'adTA5k24pPOTSADSL2':adTA5k24pPOTSADSL2,'adTA5k32pADSL2int':adTA5k32pADSL2int,'adTAOctAdslmg':adTAOctAdslmg,'adTAOctAdslProv':adTAOctAdslProv,'adTAOctAdslProv2':adTAOctAdslProv2,'adTAOctAdslConfProfileExtTable':adTAOctAdslConfProfileExtTable,'adTAOctAdslConfProfileExtEntry':adTAOctAdslConfProfileExtEntry,'adTAOctAdslConfProfileLineType':adTAOctAdslConfProfileLineType,'adTAOctAdslConfProfileServiceMode':adTAOctAdslConfProfileServiceMode,'adTAOctAdslConfProfileIndexApplied':adTAOctAdslConfProfileIndexApplied,'adTAOctAdslConfProfileName':adTAOctAdslConfProfileName,'adTAOctAdslAtucConfProfileInterleaveMinINP':adTAOctAdslAtucConfProfileInterleaveMinINP,'adTAOctAdslAturConfProfileInterleaveMinINP':adTAOctAdslAturConfProfileInterleaveMinINP,'adTAOctAdslAtucConfProfileInterleaveMinInpRev2':adTAOctAdslAtucConfProfileInterleaveMinInpRev2,'adTAOctAdslAturConfProfileInterleaveMinInpRev2':adTAOctAdslAturConfProfileInterleaveMinInpRev2,'adTAOctAdslConfLineTable':adTAOctAdslConfLineTable,'adTAOctAdslConfLineEntry':adTAOctAdslConfLineEntry,'adTAOctAdslHamBandMask':adTAOctAdslHamBandMask,'adTAOctAdslCabinetMode':adTAOctAdslCabinetMode,'adTAOctAdslPowerThreshold':adTAOctAdslPowerThreshold,'adTAOctAdslAtucCarrierMask':adTAOctAdslAtucCarrierMask,'adTAOctAdslAturCarrierMask':adTAOctAdslAturCarrierMask,'adTAOctAdslStatus2':adTAOctAdslStatus2,'adTAOctAdslLineTable':adTAOctAdslLineTable,'adTAOctAdslLineEntry':adTAOctAdslLineEntry,'adTAOctAdslCurrLinkStatus':adTAOctAdslCurrLinkStatus,'adTAOctAdslCurrStandard':adTAOctAdslCurrStandard,'adTAOctAdslBitAllocationMap':adTAOctAdslBitAllocationMap,'adTAOctAdslBitAllocationMapGroup2':adTAOctAdslBitAllocationMapGroup2,'adTAOctAdslUsSnrMarginMap':adTAOctAdslUsSnrMarginMap,'adTAOctAdslAtucPhysTable':adTAOctAdslAtucPhysTable,'adTAOctAdslAtucPhysEntry':adTAOctAdslAtucPhysEntry,'adTAOctAdslAtucNumParityBytes':adTAOctAdslAtucNumParityBytes,'adTAOctAdslAtucFramesPerCodeword':adTAOctAdslAtucFramesPerCodeword,'adTAOctAdslAtucInterleavingDepth':adTAOctAdslAtucInterleavingDepth,'adTAOctAdslAturPhysTable':adTAOctAdslAturPhysTable,'adTAOctAdslAturPhysEntry':adTAOctAdslAturPhysEntry,'adTAOctAdslAturNumParityBytes':adTAOctAdslAturNumParityBytes,'adTAOctAdslAturFramesPerCodeword':adTAOctAdslAturFramesPerCodeword,'adTAOctAdslAturInterleavingDepth':adTAOctAdslAturInterleavingDepth,'adTAOctAdslAturCapabilities':adTAOctAdslAturCapabilities,'adTAOctAdslAturInvProviderCode':adTAOctAdslAturInvProviderCode,'adTAOctAdslAtucChanTable':adTAOctAdslAtucChanTable,'adTAOctAdslAtucChanEntry':adTAOctAdslAtucChanEntry,'adTAOctAdslAtucChanINP':adTAOctAdslAtucChanINP,'adTAOctAdslAtucRelativeCap':adTAOctAdslAtucRelativeCap,'adTAOctAdslAturChanTable':adTAOctAdslAturChanTable,'adTAOctAdslAturChanEntry':adTAOctAdslAturChanEntry,'adTAOctAdslAturChanINP':adTAOctAdslAturChanINP,'adTAOctAdslAturRelativeCap':adTAOctAdslAturRelativeCap,'adTAOctAdslAtmAtucCellCountTable':adTAOctAdslAtmAtucCellCountTable,'adTAOctAdslAtmAtucCellCountEntry':adTAOctAdslAtmAtucCellCountEntry,'adTAOctAdslAtmAtucCellCount':adTAOctAdslAtmAtucCellCount,'adTAOctAdslAtmAtucIdleCellCount':adTAOctAdslAtmAtucIdleCellCount,'adTAOctAdslAtmAtucHecErrorCount':adTAOctAdslAtmAtucHecErrorCount,'adTAOctAdslAtmAturCellCountTable':adTAOctAdslAtmAturCellCountTable,'adTAOctAdslAtmAturCellCountEntry':adTAOctAdslAtmAturCellCountEntry,'adTAOctAdslAtmAturCellCount':adTAOctAdslAtmAturCellCount,'adTAOctAdslAtmAturIdleCellCount':adTAOctAdslAtmAturIdleCellCount,'adTAOctAdslID':adTAOctAdslID})