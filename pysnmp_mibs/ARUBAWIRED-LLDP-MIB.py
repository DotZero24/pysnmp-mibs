_Ah='arubaWiredLldpScalarGroup'
_Ag='arubaWiredLldpXdot3RemSysGroup'
_Af='arubaWiredLldpXdot3LocSysGroup'
_Ae='arubaWiredLldpMgmtAddrVlanId'
_Ad='arubaWiredLldpXdot3RemPowerDownTime'
_Ac='arubaWiredLldpXdot3RemPowerDownRequest'
_Ab='arubaWiredLldpXdot3RemAutoclassRequest'
_Aa='arubaWiredLldpXdot3RemPSEMaxAvailPower'
_AZ='arubaWiredLldpXdot3RemPD4PID'
_AY='arubaWiredLldpXdot3RemPDLoad'
_AX='arubaWiredLldpXdot3RemPowerTypeExt'
_AW='arubaWiredLldpXdot3RemPowerClassExt'
_AV='arubaWiredLldpXdot3RemPowerClassExtB'
_AU='arubaWiredLldpXdot3RemPowerClassExtA'
_AT='arubaWiredLldpXdot3RemPDPoweredStatus'
_AS='arubaWiredLldpXdot3RemPSEAllocatedPowerValueB'
_AR='arubaWiredLldpXdot3RemPSEAllocatedPowerValueA'
_AQ='arubaWiredLldpXdot3RemPSEAllocatedPowerValue'
_AP='arubaWiredLldpXdot3RemPDRequestedPowerValueB'
_AO='arubaWiredLldpXdot3RemPDRequestedPowerValueA'
_AN='arubaWiredLldpXdot3RemPDRequestedPowerValue'
_AM='arubaWiredLldpXdot3RemPowerPriority'
_AL='arubaWiredLldpXdot3RemPowerSource'
_AK='arubaWiredLldpXdot3RemPowerType'
_AJ='arubaWiredLldpXdot3RemPowerClass'
_AI='arubaWiredLldpXdot3RemPowerPairs'
_AH='arubaWiredLldpXdot3RemPowerPairControlable'
_AG='arubaWiredLldpXdot3RemPowerMDIEnabled'
_AF='arubaWiredLldpXdot3RemPowerMDISupported'
_AE='arubaWiredLldpXdot3RemPowerPortClass'
_AD='arubaWiredLldpLocPdTlvSentType'
_AC='arubaWiredLldpLocPseTlvSentType'
_AB='arubaWiredLldpXdot3LocAutoclassCompleted'
_AA='arubaWiredLldpXdot3LocPSEAutoclassSupport'
_A9='arubaWiredLldpXdot3LocPSEMaxAvailPower'
_A8='arubaWiredLldpXdot3LocPDLoad'
_A7='arubaWiredLldpXdot3LocPowerTypeExt'
_A6='arubaWiredLldpXdot3LocPowerClassExt'
_A5='arubaWiredLldpXdot3LocPowerClassExtB'
_A4='arubaWiredLldpXdot3LocPowerClassExtA'
_A3='arubaWiredLldpXdot3LocPowerPairsExt'
_A2='arubaWiredLldpXdot3LocPSEPoweringStatus'
_A1='arubaWiredLldpXdot3LocPSEAllocatedPowerValueB'
_A0='arubaWiredLldpXdot3LocPSEAllocatedPowerValueA'
_z='arubaWiredLldpXdot3LocPSEAllocatedPowerValue'
_y='arubaWiredLldpXdot3LocPDRequestedPowerValueB'
_x='arubaWiredLldpXdot3LocPDRequestedPowerValueA'
_w='arubaWiredLldpXdot3LocPDRequestedPowerValue'
_v='arubaWiredLldpXdot3LocPowerPriority'
_u='arubaWiredLldpXdot3LocPowerSource'
_t='arubaWiredLldpXdot3LocPowerType'
_s='arubaWiredLldpXdot3LocPowerClass'
_r='arubaWiredLldpXdot3LocPowerPairs'
_q='arubaWiredLldpXdot3LocPowerPairControlable'
_p='arubaWiredLldpXdot3LocPowerMDIEnabled'
_o='arubaWiredLldpXdot3LocPowerMDISupported'
_n='arubaWiredLldpXdot3LocPowerPortClass'
_m='dot3-ext'
_l='type4dualsigPD'
_k='type4singlesigPD'
_j='type3dualsigPD'
_i='type3singlesigPD'
_h='type4PSE'
_g='type3PSE'
_f='class8'
_e='class7'
_d='class6'
_c='dualsig'
_b='fourPdualsigPD'
_a='critical'
_Z='type1PD'
_Y='type1PSE'
_X='type2PD'
_W='type2PSE'
_V='class0'
_U='pairSpare'
_T='pairSignal'
_S='pClassPD'
_R='pClassPSE'
_Q='lldpRemTimeMark'
_P='lldpRemLocalPortNum'
_O='lldpRemIndex'
_N='lldpLocPortNum'
_M='singlesig'
_L='unknown'
_K='LLDP-MIB'
_J='class5'
_I='class4'
_H='class3'
_G='class2'
_F='class1'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ARUBAWIRED-LLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
lldpLocPortNum,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_K,_N,_O,_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
arubaWiredLldpMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,9))
if mibBuilder.loadTexts:arubaWiredLldpMIB.setRevisions(('2022-11-24 00:00','2020-10-22 00:00','2019-04-15 00:00'))
_ArubaWiredLldpXdot3Objects_ObjectIdentity=ObjectIdentity
arubaWiredLldpXdot3Objects=_ArubaWiredLldpXdot3Objects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,1))
_ArubaWiredLldpXdot3LocalData_ObjectIdentity=ObjectIdentity
arubaWiredLldpXdot3LocalData=_ArubaWiredLldpXdot3LocalData_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,1,1))
_ArubaWiredLldpXdot3LocPowerTable_Object=MibTable
arubaWiredLldpXdot3LocPowerTable=_ArubaWiredLldpXdot3LocPowerTable_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1))
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerTable.setStatus(_A)
_ArubaWiredLldpXdot3LocPowerEntry_Object=MibTableRow
arubaWiredLldpXdot3LocPowerEntry=_ArubaWiredLldpXdot3LocPowerEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1))
arubaWiredLldpXdot3LocPowerEntry.setIndexNames((0,_K,_N))
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerEntry.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerPortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ArubaWiredLldpXdot3LocPowerPortClass_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerPortClass_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerPortClass=_ArubaWiredLldpXdot3LocPowerPortClass_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,1),_ArubaWiredLldpXdot3LocPowerPortClass_Type())
arubaWiredLldpXdot3LocPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerPortClass.setStatus(_A)
_ArubaWiredLldpXdot3LocPowerMDISupported_Type=TruthValue
_ArubaWiredLldpXdot3LocPowerMDISupported_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerMDISupported=_ArubaWiredLldpXdot3LocPowerMDISupported_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,2),_ArubaWiredLldpXdot3LocPowerMDISupported_Type())
arubaWiredLldpXdot3LocPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerMDISupported.setStatus(_A)
_ArubaWiredLldpXdot3LocPowerMDIEnabled_Type=TruthValue
_ArubaWiredLldpXdot3LocPowerMDIEnabled_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerMDIEnabled=_ArubaWiredLldpXdot3LocPowerMDIEnabled_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,3),_ArubaWiredLldpXdot3LocPowerMDIEnabled_Type())
arubaWiredLldpXdot3LocPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerMDIEnabled.setStatus(_A)
_ArubaWiredLldpXdot3LocPowerPairControlable_Type=TruthValue
_ArubaWiredLldpXdot3LocPowerPairControlable_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerPairControlable=_ArubaWiredLldpXdot3LocPowerPairControlable_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,4),_ArubaWiredLldpXdot3LocPowerPairControlable_Type())
arubaWiredLldpXdot3LocPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerPairControlable.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ArubaWiredLldpXdot3LocPowerPairs_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerPairs_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerPairs=_ArubaWiredLldpXdot3LocPowerPairs_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,5),_ArubaWiredLldpXdot3LocPowerPairs_Type())
arubaWiredLldpXdot3LocPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerPairs.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),(_F,2),(_G,3),(_H,4),(_I,5)))
_ArubaWiredLldpXdot3LocPowerClass_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerClass_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerClass=_ArubaWiredLldpXdot3LocPowerClass_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,6),_ArubaWiredLldpXdot3LocPowerClass_Type())
arubaWiredLldpXdot3LocPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerClass.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4)))
_ArubaWiredLldpXdot3LocPowerType_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerType_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerType=_ArubaWiredLldpXdot3LocPowerType_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,7),_ArubaWiredLldpXdot3LocPowerType_Type())
arubaWiredLldpXdot3LocPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerType.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('primary',2),('backup',3),('reserved',4)))
_ArubaWiredLldpXdot3LocPowerSource_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerSource_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerSource=_ArubaWiredLldpXdot3LocPowerSource_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,8),_ArubaWiredLldpXdot3LocPowerSource_Type())
arubaWiredLldpXdot3LocPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerSource.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_a,2),('high',3),('low',4)))
_ArubaWiredLldpXdot3LocPowerPriority_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerPriority_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerPriority=_ArubaWiredLldpXdot3LocPowerPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,9),_ArubaWiredLldpXdot3LocPowerPriority_Type())
arubaWiredLldpXdot3LocPowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerPriority.setStatus(_A)
class _ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type.__name__=_D
_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Object=MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValue=_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,10),_ArubaWiredLldpXdot3LocPDRequestedPowerValue_Type())
arubaWiredLldpXdot3LocPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPDRequestedPowerValue.setStatus(_A)
class _ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type.__name__=_D
_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Object=MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValueA=_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,11),_ArubaWiredLldpXdot3LocPDRequestedPowerValueA_Type())
arubaWiredLldpXdot3LocPDRequestedPowerValueA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPDRequestedPowerValueA.setStatus(_A)
class _ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type.__name__=_D
_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Object=MibTableColumn
arubaWiredLldpXdot3LocPDRequestedPowerValueB=_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,12),_ArubaWiredLldpXdot3LocPDRequestedPowerValueB_Type())
arubaWiredLldpXdot3LocPDRequestedPowerValueB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPDRequestedPowerValueB.setStatus(_A)
class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type.__name__=_D
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValue=_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,13),_ArubaWiredLldpXdot3LocPSEAllocatedPowerValue_Type())
arubaWiredLldpXdot3LocPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEAllocatedPowerValue.setStatus(_A)
class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type.__name__=_D
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValueA=_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,14),_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueA_Type())
arubaWiredLldpXdot3LocPSEAllocatedPowerValueA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEAllocatedPowerValueA.setStatus(_A)
class _ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type.__name__=_D
_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEAllocatedPowerValueB=_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,15),_ArubaWiredLldpXdot3LocPSEAllocatedPowerValueB_Type())
arubaWiredLldpXdot3LocPSEAllocatedPowerValueB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEAllocatedPowerValueB.setStatus(_A)
class _ArubaWiredLldpXdot3LocPSEPoweringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('twoPair',1),('fourPsinglesigPD',2),(_b,3)))
_ArubaWiredLldpXdot3LocPSEPoweringStatus_Type.__name__=_D
_ArubaWiredLldpXdot3LocPSEPoweringStatus_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEPoweringStatus=_ArubaWiredLldpXdot3LocPSEPoweringStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,16),_ArubaWiredLldpXdot3LocPSEPoweringStatus_Type())
arubaWiredLldpXdot3LocPSEPoweringStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEPoweringStatus.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerPairsExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('altA',1),('altB',2),('both',3)))
_ArubaWiredLldpXdot3LocPowerPairsExt_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerPairsExt_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerPairsExt=_ArubaWiredLldpXdot3LocPowerPairsExt_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,17),_ArubaWiredLldpXdot3LocPowerPairsExt_Type())
arubaWiredLldpXdot3LocPowerPairsExt.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerPairsExt.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerClassExtA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_ArubaWiredLldpXdot3LocPowerClassExtA_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerClassExtA_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerClassExtA=_ArubaWiredLldpXdot3LocPowerClassExtA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,18),_ArubaWiredLldpXdot3LocPowerClassExtA_Type())
arubaWiredLldpXdot3LocPowerClassExtA.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerClassExtA.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerClassExtB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_ArubaWiredLldpXdot3LocPowerClassExtB_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerClassExtB_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerClassExtB=_ArubaWiredLldpXdot3LocPowerClassExtB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,19),_ArubaWiredLldpXdot3LocPowerClassExtB_Type())
arubaWiredLldpXdot3LocPowerClassExtB.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerClassExtB.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerClassExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_c,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_d,7),(_e,8),(_f,9)))
_ArubaWiredLldpXdot3LocPowerClassExt_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerClassExt_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerClassExt=_ArubaWiredLldpXdot3LocPowerClassExt_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,20),_ArubaWiredLldpXdot3LocPowerClassExt_Type())
arubaWiredLldpXdot3LocPowerClassExt.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerClassExt.setStatus(_A)
class _ArubaWiredLldpXdot3LocPowerTypeExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_ArubaWiredLldpXdot3LocPowerTypeExt_Type.__name__=_D
_ArubaWiredLldpXdot3LocPowerTypeExt_Object=MibTableColumn
arubaWiredLldpXdot3LocPowerTypeExt=_ArubaWiredLldpXdot3LocPowerTypeExt_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,21),_ArubaWiredLldpXdot3LocPowerTypeExt_Type())
arubaWiredLldpXdot3LocPowerTypeExt.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPowerTypeExt.setStatus(_A)
_ArubaWiredLldpXdot3LocPDLoad_Type=TruthValue
_ArubaWiredLldpXdot3LocPDLoad_Object=MibTableColumn
arubaWiredLldpXdot3LocPDLoad=_ArubaWiredLldpXdot3LocPDLoad_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,22),_ArubaWiredLldpXdot3LocPDLoad_Type())
arubaWiredLldpXdot3LocPDLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPDLoad.setStatus(_A)
class _ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type.__name__=_D
_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEMaxAvailPower=_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,23),_ArubaWiredLldpXdot3LocPSEMaxAvailPower_Type())
arubaWiredLldpXdot3LocPSEMaxAvailPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEMaxAvailPower.setStatus(_A)
_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Type=TruthValue
_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Object=MibTableColumn
arubaWiredLldpXdot3LocPSEAutoclassSupport=_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,24),_ArubaWiredLldpXdot3LocPSEAutoclassSupport_Type())
arubaWiredLldpXdot3LocPSEAutoclassSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocPSEAutoclassSupport.setStatus(_A)
_ArubaWiredLldpXdot3LocAutoclassCompleted_Type=TruthValue
_ArubaWiredLldpXdot3LocAutoclassCompleted_Object=MibTableColumn
arubaWiredLldpXdot3LocAutoclassCompleted=_ArubaWiredLldpXdot3LocAutoclassCompleted_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,25),_ArubaWiredLldpXdot3LocAutoclassCompleted_Type())
arubaWiredLldpXdot3LocAutoclassCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocAutoclassCompleted.setStatus(_A)
class _ArubaWiredLldpLocPseTlvSentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('med',1),('dot3',2),(_m,3)))
_ArubaWiredLldpLocPseTlvSentType_Type.__name__=_D
_ArubaWiredLldpLocPseTlvSentType_Object=MibTableColumn
arubaWiredLldpLocPseTlvSentType=_ArubaWiredLldpLocPseTlvSentType_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,26),_ArubaWiredLldpLocPseTlvSentType_Type())
arubaWiredLldpLocPseTlvSentType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpLocPseTlvSentType.setStatus(_A)
class _ArubaWiredLldpLocPdTlvSentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('med',1),('dot3',2),(_m,3),('medanddot3',4),('medanddot3-ext',5)))
_ArubaWiredLldpLocPdTlvSentType_Type.__name__=_D
_ArubaWiredLldpLocPdTlvSentType_Object=MibTableColumn
arubaWiredLldpLocPdTlvSentType=_ArubaWiredLldpLocPdTlvSentType_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,1,1,1,27),_ArubaWiredLldpLocPdTlvSentType_Type())
arubaWiredLldpLocPdTlvSentType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpLocPdTlvSentType.setStatus(_A)
_ArubaWiredLldpXdot3RemoteData_ObjectIdentity=ObjectIdentity
arubaWiredLldpXdot3RemoteData=_ArubaWiredLldpXdot3RemoteData_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,1,2))
_ArubaWiredLldpXdot3RemPowerTable_Object=MibTable
arubaWiredLldpXdot3RemPowerTable=_ArubaWiredLldpXdot3RemPowerTable_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1))
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerTable.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerEntry_Object=MibTableRow
arubaWiredLldpXdot3RemPowerEntry=_ArubaWiredLldpXdot3RemPowerEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1))
arubaWiredLldpXdot3RemPowerEntry.setIndexNames((0,_K,_Q),(0,_K,_P),(0,_K,_O))
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerEntry.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerPortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_ArubaWiredLldpXdot3RemPowerPortClass_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerPortClass_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerPortClass=_ArubaWiredLldpXdot3RemPowerPortClass_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,1),_ArubaWiredLldpXdot3RemPowerPortClass_Type())
arubaWiredLldpXdot3RemPowerPortClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerPortClass.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerMDISupported_Type=TruthValue
_ArubaWiredLldpXdot3RemPowerMDISupported_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerMDISupported=_ArubaWiredLldpXdot3RemPowerMDISupported_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,2),_ArubaWiredLldpXdot3RemPowerMDISupported_Type())
arubaWiredLldpXdot3RemPowerMDISupported.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerMDISupported.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerMDIEnabled_Type=TruthValue
_ArubaWiredLldpXdot3RemPowerMDIEnabled_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerMDIEnabled=_ArubaWiredLldpXdot3RemPowerMDIEnabled_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,3),_ArubaWiredLldpXdot3RemPowerMDIEnabled_Type())
arubaWiredLldpXdot3RemPowerMDIEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerMDIEnabled.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerPairControlable_Type=TruthValue
_ArubaWiredLldpXdot3RemPowerPairControlable_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerPairControlable=_ArubaWiredLldpXdot3RemPowerPairControlable_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,4),_ArubaWiredLldpXdot3RemPowerPairControlable_Type())
arubaWiredLldpXdot3RemPowerPairControlable.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerPairControlable.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ArubaWiredLldpXdot3RemPowerPairs_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerPairs_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerPairs=_ArubaWiredLldpXdot3RemPowerPairs_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,5),_ArubaWiredLldpXdot3RemPowerPairs_Type())
arubaWiredLldpXdot3RemPowerPairs.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerPairs.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),(_F,2),(_G,3),(_H,4),(_I,5)))
_ArubaWiredLldpXdot3RemPowerClass_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerClass_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerClass=_ArubaWiredLldpXdot3RemPowerClass_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,6),_ArubaWiredLldpXdot3RemPowerClass_Type())
arubaWiredLldpXdot3RemPowerClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerClass.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4)))
_ArubaWiredLldpXdot3RemPowerType_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerType_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerType=_ArubaWiredLldpXdot3RemPowerType_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,7),_ArubaWiredLldpXdot3RemPowerType_Type())
arubaWiredLldpXdot3RemPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerType.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('pse',2),('local',3),('pseAndLocal',4)))
_ArubaWiredLldpXdot3RemPowerSource_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerSource_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerSource=_ArubaWiredLldpXdot3RemPowerSource_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,8),_ArubaWiredLldpXdot3RemPowerSource_Type())
arubaWiredLldpXdot3RemPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerSource.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_a,2),('high',3),('low',4)))
_ArubaWiredLldpXdot3RemPowerPriority_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerPriority_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerPriority=_ArubaWiredLldpXdot3RemPowerPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,9),_ArubaWiredLldpXdot3RemPowerPriority_Type())
arubaWiredLldpXdot3RemPowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerPriority.setStatus(_A)
class _ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type.__name__=_D
_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Object=MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValue=_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,10),_ArubaWiredLldpXdot3RemPDRequestedPowerValue_Type())
arubaWiredLldpXdot3RemPDRequestedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPDRequestedPowerValue.setStatus(_A)
class _ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type.__name__=_D
_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Object=MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValueA=_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,11),_ArubaWiredLldpXdot3RemPDRequestedPowerValueA_Type())
arubaWiredLldpXdot3RemPDRequestedPowerValueA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPDRequestedPowerValueA.setStatus(_A)
class _ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type.__name__=_D
_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Object=MibTableColumn
arubaWiredLldpXdot3RemPDRequestedPowerValueB=_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,12),_ArubaWiredLldpXdot3RemPDRequestedPowerValueB_Type())
arubaWiredLldpXdot3RemPDRequestedPowerValueB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPDRequestedPowerValueB.setStatus(_A)
class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type.__name__=_D
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Object=MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValue=_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,13),_ArubaWiredLldpXdot3RemPSEAllocatedPowerValue_Type())
arubaWiredLldpXdot3RemPSEAllocatedPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPSEAllocatedPowerValue.setStatus(_A)
class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type.__name__=_D
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Object=MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValueA=_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,14),_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueA_Type())
arubaWiredLldpXdot3RemPSEAllocatedPowerValueA.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPSEAllocatedPowerValueA.setStatus(_A)
class _ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,499))
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type.__name__=_D
_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Object=MibTableColumn
arubaWiredLldpXdot3RemPSEAllocatedPowerValueB=_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,15),_ArubaWiredLldpXdot3RemPSEAllocatedPowerValueB_Type())
arubaWiredLldpXdot3RemPSEAllocatedPowerValueB.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPSEAllocatedPowerValueB.setStatus(_A)
class _ArubaWiredLldpXdot3RemPDPoweredStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singlesigPD',1),('twoPdualsigPD',2),(_b,3)))
_ArubaWiredLldpXdot3RemPDPoweredStatus_Type.__name__=_D
_ArubaWiredLldpXdot3RemPDPoweredStatus_Object=MibTableColumn
arubaWiredLldpXdot3RemPDPoweredStatus=_ArubaWiredLldpXdot3RemPDPoweredStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,16),_ArubaWiredLldpXdot3RemPDPoweredStatus_Type())
arubaWiredLldpXdot3RemPDPoweredStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPDPoweredStatus.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerClassExtA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_ArubaWiredLldpXdot3RemPowerClassExtA_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerClassExtA_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerClassExtA=_ArubaWiredLldpXdot3RemPowerClassExtA_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,17),_ArubaWiredLldpXdot3RemPowerClassExtA_Type())
arubaWiredLldpXdot3RemPowerClassExtA.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerClassExtA.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerClassExtB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_ArubaWiredLldpXdot3RemPowerClassExtB_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerClassExtB_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerClassExtB=_ArubaWiredLldpXdot3RemPowerClassExtB_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,18),_ArubaWiredLldpXdot3RemPowerClassExtB_Type())
arubaWiredLldpXdot3RemPowerClassExtB.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerClassExtB.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerClassExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_c,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_d,7),(_e,8),(_f,9)))
_ArubaWiredLldpXdot3RemPowerClassExt_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerClassExt_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerClassExt=_ArubaWiredLldpXdot3RemPowerClassExt_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,19),_ArubaWiredLldpXdot3RemPowerClassExt_Type())
arubaWiredLldpXdot3RemPowerClassExt.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerClassExt.setStatus(_A)
class _ArubaWiredLldpXdot3RemPowerTypeExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6)))
_ArubaWiredLldpXdot3RemPowerTypeExt_Type.__name__=_D
_ArubaWiredLldpXdot3RemPowerTypeExt_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerTypeExt=_ArubaWiredLldpXdot3RemPowerTypeExt_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,20),_ArubaWiredLldpXdot3RemPowerTypeExt_Type())
arubaWiredLldpXdot3RemPowerTypeExt.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerTypeExt.setStatus(_A)
_ArubaWiredLldpXdot3RemPDLoad_Type=TruthValue
_ArubaWiredLldpXdot3RemPDLoad_Object=MibTableColumn
arubaWiredLldpXdot3RemPDLoad=_ArubaWiredLldpXdot3RemPDLoad_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,21),_ArubaWiredLldpXdot3RemPDLoad_Type())
arubaWiredLldpXdot3RemPDLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPDLoad.setStatus(_A)
_ArubaWiredLldpXdot3RemPD4PID_Type=TruthValue
_ArubaWiredLldpXdot3RemPD4PID_Object=MibTableColumn
arubaWiredLldpXdot3RemPD4PID=_ArubaWiredLldpXdot3RemPD4PID_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,22),_ArubaWiredLldpXdot3RemPD4PID_Type())
arubaWiredLldpXdot3RemPD4PID.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPD4PID.setStatus(_A)
class _ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type.__name__=_D
_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Object=MibTableColumn
arubaWiredLldpXdot3RemPSEMaxAvailPower=_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,23),_ArubaWiredLldpXdot3RemPSEMaxAvailPower_Type())
arubaWiredLldpXdot3RemPSEMaxAvailPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPSEMaxAvailPower.setStatus(_A)
_ArubaWiredLldpXdot3RemAutoclassRequest_Type=TruthValue
_ArubaWiredLldpXdot3RemAutoclassRequest_Object=MibTableColumn
arubaWiredLldpXdot3RemAutoclassRequest=_ArubaWiredLldpXdot3RemAutoclassRequest_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,24),_ArubaWiredLldpXdot3RemAutoclassRequest_Type())
arubaWiredLldpXdot3RemAutoclassRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemAutoclassRequest.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerDownRequest_Type=Integer32
_ArubaWiredLldpXdot3RemPowerDownRequest_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerDownRequest=_ArubaWiredLldpXdot3RemPowerDownRequest_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,25),_ArubaWiredLldpXdot3RemPowerDownRequest_Type())
arubaWiredLldpXdot3RemPowerDownRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerDownRequest.setStatus(_A)
_ArubaWiredLldpXdot3RemPowerDownTime_Type=Integer32
_ArubaWiredLldpXdot3RemPowerDownTime_Object=MibTableColumn
arubaWiredLldpXdot3RemPowerDownTime=_ArubaWiredLldpXdot3RemPowerDownTime_Object((1,3,6,1,4,1,47196,4,1,1,3,9,1,2,1,1,26),_ArubaWiredLldpXdot3RemPowerDownTime_Type())
arubaWiredLldpXdot3RemPowerDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemPowerDownTime.setStatus(_A)
_ArubaWiredLldpConformance_ObjectIdentity=ObjectIdentity
arubaWiredLldpConformance=_ArubaWiredLldpConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,2))
_ArubaWiredLldpCompliances_ObjectIdentity=ObjectIdentity
arubaWiredLldpCompliances=_ArubaWiredLldpCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,2,1))
_ArubaWiredLldpGroups_ObjectIdentity=ObjectIdentity
arubaWiredLldpGroups=_ArubaWiredLldpGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,2,2))
_ArubaWiredLldpScalarConfig_ObjectIdentity=ObjectIdentity
arubaWiredLldpScalarConfig=_ArubaWiredLldpScalarConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,9,3))
class _ArubaWiredLldpMgmtAddrVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ArubaWiredLldpMgmtAddrVlanId_Type.__name__=_D
_ArubaWiredLldpMgmtAddrVlanId_Object=MibScalar
arubaWiredLldpMgmtAddrVlanId=_ArubaWiredLldpMgmtAddrVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,9,3,1),_ArubaWiredLldpMgmtAddrVlanId_Type())
arubaWiredLldpMgmtAddrVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredLldpMgmtAddrVlanId.setStatus(_A)
arubaWiredLldpXdot3LocSysGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,9,2,2,1))
arubaWiredLldpXdot3LocSysGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:arubaWiredLldpXdot3LocSysGroup.setStatus(_A)
arubaWiredLldpXdot3RemSysGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,9,2,2,2))
arubaWiredLldpXdot3RemSysGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:arubaWiredLldpXdot3RemSysGroup.setStatus(_A)
arubaWiredLldpScalarGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,9,2,2,3))
arubaWiredLldpScalarGroup.setObjects((_B,_Ae))
if mibBuilder.loadTexts:arubaWiredLldpScalarGroup.setStatus(_A)
arubaWiredLldpXdot3Compliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,9,2,1,1))
arubaWiredLldpXdot3Compliance.setObjects(*((_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:arubaWiredLldpXdot3Compliance.setStatus(_A)
arubaWiredLldpScalarCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,9,2,1,2))
arubaWiredLldpScalarCompliance.setObjects((_B,_Ah))
if mibBuilder.loadTexts:arubaWiredLldpScalarCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredLldpMIB':arubaWiredLldpMIB,'arubaWiredLldpXdot3Objects':arubaWiredLldpXdot3Objects,'arubaWiredLldpXdot3LocalData':arubaWiredLldpXdot3LocalData,'arubaWiredLldpXdot3LocPowerTable':arubaWiredLldpXdot3LocPowerTable,'arubaWiredLldpXdot3LocPowerEntry':arubaWiredLldpXdot3LocPowerEntry,_n:arubaWiredLldpXdot3LocPowerPortClass,_o:arubaWiredLldpXdot3LocPowerMDISupported,_p:arubaWiredLldpXdot3LocPowerMDIEnabled,_q:arubaWiredLldpXdot3LocPowerPairControlable,_r:arubaWiredLldpXdot3LocPowerPairs,_s:arubaWiredLldpXdot3LocPowerClass,_t:arubaWiredLldpXdot3LocPowerType,_u:arubaWiredLldpXdot3LocPowerSource,_v:arubaWiredLldpXdot3LocPowerPriority,_w:arubaWiredLldpXdot3LocPDRequestedPowerValue,_x:arubaWiredLldpXdot3LocPDRequestedPowerValueA,_y:arubaWiredLldpXdot3LocPDRequestedPowerValueB,_z:arubaWiredLldpXdot3LocPSEAllocatedPowerValue,_A0:arubaWiredLldpXdot3LocPSEAllocatedPowerValueA,_A1:arubaWiredLldpXdot3LocPSEAllocatedPowerValueB,_A2:arubaWiredLldpXdot3LocPSEPoweringStatus,_A3:arubaWiredLldpXdot3LocPowerPairsExt,_A4:arubaWiredLldpXdot3LocPowerClassExtA,_A5:arubaWiredLldpXdot3LocPowerClassExtB,_A6:arubaWiredLldpXdot3LocPowerClassExt,_A7:arubaWiredLldpXdot3LocPowerTypeExt,_A8:arubaWiredLldpXdot3LocPDLoad,_A9:arubaWiredLldpXdot3LocPSEMaxAvailPower,_AA:arubaWiredLldpXdot3LocPSEAutoclassSupport,_AB:arubaWiredLldpXdot3LocAutoclassCompleted,_AC:arubaWiredLldpLocPseTlvSentType,_AD:arubaWiredLldpLocPdTlvSentType,'arubaWiredLldpXdot3RemoteData':arubaWiredLldpXdot3RemoteData,'arubaWiredLldpXdot3RemPowerTable':arubaWiredLldpXdot3RemPowerTable,'arubaWiredLldpXdot3RemPowerEntry':arubaWiredLldpXdot3RemPowerEntry,_AE:arubaWiredLldpXdot3RemPowerPortClass,_AF:arubaWiredLldpXdot3RemPowerMDISupported,_AG:arubaWiredLldpXdot3RemPowerMDIEnabled,_AH:arubaWiredLldpXdot3RemPowerPairControlable,_AI:arubaWiredLldpXdot3RemPowerPairs,_AJ:arubaWiredLldpXdot3RemPowerClass,_AK:arubaWiredLldpXdot3RemPowerType,_AL:arubaWiredLldpXdot3RemPowerSource,_AM:arubaWiredLldpXdot3RemPowerPriority,_AN:arubaWiredLldpXdot3RemPDRequestedPowerValue,_AO:arubaWiredLldpXdot3RemPDRequestedPowerValueA,_AP:arubaWiredLldpXdot3RemPDRequestedPowerValueB,_AQ:arubaWiredLldpXdot3RemPSEAllocatedPowerValue,_AR:arubaWiredLldpXdot3RemPSEAllocatedPowerValueA,_AS:arubaWiredLldpXdot3RemPSEAllocatedPowerValueB,_AT:arubaWiredLldpXdot3RemPDPoweredStatus,_AU:arubaWiredLldpXdot3RemPowerClassExtA,_AV:arubaWiredLldpXdot3RemPowerClassExtB,_AW:arubaWiredLldpXdot3RemPowerClassExt,_AX:arubaWiredLldpXdot3RemPowerTypeExt,_AY:arubaWiredLldpXdot3RemPDLoad,_AZ:arubaWiredLldpXdot3RemPD4PID,_Aa:arubaWiredLldpXdot3RemPSEMaxAvailPower,_Ab:arubaWiredLldpXdot3RemAutoclassRequest,_Ac:arubaWiredLldpXdot3RemPowerDownRequest,_Ad:arubaWiredLldpXdot3RemPowerDownTime,'arubaWiredLldpConformance':arubaWiredLldpConformance,'arubaWiredLldpCompliances':arubaWiredLldpCompliances,'arubaWiredLldpXdot3Compliance':arubaWiredLldpXdot3Compliance,'arubaWiredLldpScalarCompliance':arubaWiredLldpScalarCompliance,'arubaWiredLldpGroups':arubaWiredLldpGroups,_Af:arubaWiredLldpXdot3LocSysGroup,_Ag:arubaWiredLldpXdot3RemSysGroup,_Ah:arubaWiredLldpScalarGroup,'arubaWiredLldpScalarConfig':arubaWiredLldpScalarConfig,_Ae:arubaWiredLldpMgmtAddrVlanId})