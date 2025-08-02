_N='hwVoAnalogIfEMTimerPortNumber'
_M='hwVoAnalogIfEMConfigPortNumber'
_L='hwVoAnalogIfFXOTimerPortNumber'
_K='hwVoAnalogIfFXOConfigPortNumber'
_J='hwVoAnalogIfFXSTimerPortNumber'
_I='groundStart'
_H='loopStart'
_G='hwVoAnalogIfFXSConfigPortNumber'
_F='hwVoAnalogIfConfigPortNumber'
_E='HUAWEI-VO-ANALOG-IF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceAnalogInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,3))
if mibBuilder.loadTexts:hwVoiceAnalogInterfaceMIB.setRevisions(('2004-04-08 13:45',))
_HwVoAnalogIfCommonObjects_ObjectIdentity=ObjectIdentity
hwVoAnalogIfCommonObjects=_HwVoAnalogIfCommonObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,3,1))
_HwVoAnalogIfCommonConfigTable_Object=MibTable
hwVoAnalogIfCommonConfigTable=_HwVoAnalogIfCommonConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1))
if mibBuilder.loadTexts:hwVoAnalogIfCommonConfigTable.setStatus(_A)
_HwVoAnalogIfCommonConfigEntry_Object=MibTableRow
hwVoAnalogIfCommonConfigEntry=_HwVoAnalogIfCommonConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1))
hwVoAnalogIfCommonConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hwVoAnalogIfCommonConfigEntry.setStatus(_A)
_HwVoAnalogIfConfigPortNumber_Type=Integer32
_HwVoAnalogIfConfigPortNumber_Object=MibTableColumn
hwVoAnalogIfConfigPortNumber=_HwVoAnalogIfConfigPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,1),_HwVoAnalogIfConfigPortNumber_Type())
hwVoAnalogIfConfigPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfConfigPortNumber.setStatus(_A)
class _HwVoAnalogIfConfigPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fxs',1),('fxo',2),('em',3)))
_HwVoAnalogIfConfigPortType_Type.__name__=_B
_HwVoAnalogIfConfigPortType_Object=MibTableColumn
hwVoAnalogIfConfigPortType=_HwVoAnalogIfConfigPortType_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,2),_HwVoAnalogIfConfigPortType_Type())
hwVoAnalogIfConfigPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfConfigPortType.setStatus(_A)
class _HwVoAnaloglfConfigPortImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('impedance600Real',1),('impedanceComplex',2)))
_HwVoAnaloglfConfigPortImpedance_Type.__name__=_B
_HwVoAnaloglfConfigPortImpedance_Object=MibTableColumn
hwVoAnaloglfConfigPortImpedance=_HwVoAnaloglfConfigPortImpedance_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,3),_HwVoAnaloglfConfigPortImpedance_Type())
hwVoAnaloglfConfigPortImpedance.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnaloglfConfigPortImpedance.setStatus(_A)
class _HwVoAnalogIfConfigInitialDigitTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HwVoAnalogIfConfigInitialDigitTimeOut_Type.__name__=_B
_HwVoAnalogIfConfigInitialDigitTimeOut_Object=MibTableColumn
hwVoAnalogIfConfigInitialDigitTimeOut=_HwVoAnalogIfConfigInitialDigitTimeOut_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,4),_HwVoAnalogIfConfigInitialDigitTimeOut_Type())
hwVoAnalogIfConfigInitialDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfConfigInitialDigitTimeOut.setStatus(_A)
class _HwVoAnalogIfConfigInterDigitTimeOut_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HwVoAnalogIfConfigInterDigitTimeOut_Type.__name__=_B
_HwVoAnalogIfConfigInterDigitTimeOut_Object=MibTableColumn
hwVoAnalogIfConfigInterDigitTimeOut=_HwVoAnalogIfConfigInterDigitTimeOut_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,5),_HwVoAnalogIfConfigInterDigitTimeOut_Type())
hwVoAnalogIfConfigInterDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfConfigInterDigitTimeOut.setStatus(_A)
class _HwVoAnalogIfConfigCallDisconnect_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_HwVoAnalogIfConfigCallDisconnect_Type.__name__=_B
_HwVoAnalogIfConfigCallDisconnect_Object=MibTableColumn
hwVoAnalogIfConfigCallDisconnect=_HwVoAnalogIfConfigCallDisconnect_Object((1,3,6,1,4,1,2011,5,25,1,3,1,1,1,6),_HwVoAnalogIfConfigCallDisconnect_Type())
hwVoAnalogIfConfigCallDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfConfigCallDisconnect.setStatus(_A)
_HwVoAnalogIfFXSObjects_ObjectIdentity=ObjectIdentity
hwVoAnalogIfFXSObjects=_HwVoAnalogIfFXSObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,3,2))
_HwVoAnalogIfFXSConfigTable_Object=MibTable
hwVoAnalogIfFXSConfigTable=_HwVoAnalogIfFXSConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,3,2,1))
if mibBuilder.loadTexts:hwVoAnalogIfFXSConfigTable.setStatus(_A)
_HwVoAnalogIfFXSConfigEntry_Object=MibTableRow
hwVoAnalogIfFXSConfigEntry=_HwVoAnalogIfFXSConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,2,1,1))
hwVoAnalogIfFXSConfigEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hwVoAnalogIfFXSConfigEntry.setStatus(_A)
_HwVoAnalogIfFXSConfigPortNumber_Type=Integer32
_HwVoAnalogIfFXSConfigPortNumber_Object=MibTableColumn
hwVoAnalogIfFXSConfigPortNumber=_HwVoAnalogIfFXSConfigPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,2,1,1,1),_HwVoAnalogIfFXSConfigPortNumber_Type())
hwVoAnalogIfFXSConfigPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXSConfigPortNumber.setStatus(_A)
class _HwVoAnalogIfFXSConfigStartMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoAnalogIfFXSConfigStartMode_Type.__name__=_B
_HwVoAnalogIfFXSConfigStartMode_Object=MibTableColumn
hwVoAnalogIfFXSConfigStartMode=_HwVoAnalogIfFXSConfigStartMode_Object((1,3,6,1,4,1,2011,5,25,1,3,2,1,1,2),_HwVoAnalogIfFXSConfigStartMode_Type())
hwVoAnalogIfFXSConfigStartMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXSConfigStartMode.setStatus(_A)
_HwVoAnalogIfFXSTimerTable_Object=MibTable
hwVoAnalogIfFXSTimerTable=_HwVoAnalogIfFXSTimerTable_Object((1,3,6,1,4,1,2011,5,25,1,3,2,3))
if mibBuilder.loadTexts:hwVoAnalogIfFXSTimerTable.setStatus(_A)
_HwVoAnalogIfFXSTimerEntry_Object=MibTableRow
hwVoAnalogIfFXSTimerEntry=_HwVoAnalogIfFXSTimerEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,2,3,1))
hwVoAnalogIfFXSTimerEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hwVoAnalogIfFXSTimerEntry.setStatus(_A)
_HwVoAnalogIfFXSTimerPortNumber_Type=Integer32
_HwVoAnalogIfFXSTimerPortNumber_Object=MibTableColumn
hwVoAnalogIfFXSTimerPortNumber=_HwVoAnalogIfFXSTimerPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,2,3,1,1),_HwVoAnalogIfFXSTimerPortNumber_Type())
hwVoAnalogIfFXSTimerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXSTimerPortNumber.setStatus(_A)
class _HwVoAnalogIfFXSTimerDtmf_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfFXSTimerDtmf_Type.__name__=_B
_HwVoAnalogIfFXSTimerDtmf_Object=MibTableColumn
hwVoAnalogIfFXSTimerDtmf=_HwVoAnalogIfFXSTimerDtmf_Object((1,3,6,1,4,1,2011,5,25,1,3,2,3,1,2),_HwVoAnalogIfFXSTimerDtmf_Type())
hwVoAnalogIfFXSTimerDtmf.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXSTimerDtmf.setStatus(_A)
class _HwVoAnalogIfFXSTimerDtmfInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfFXSTimerDtmfInterval_Type.__name__=_B
_HwVoAnalogIfFXSTimerDtmfInterval_Object=MibTableColumn
hwVoAnalogIfFXSTimerDtmfInterval=_HwVoAnalogIfFXSTimerDtmfInterval_Object((1,3,6,1,4,1,2011,5,25,1,3,2,3,1,3),_HwVoAnalogIfFXSTimerDtmfInterval_Type())
hwVoAnalogIfFXSTimerDtmfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXSTimerDtmfInterval.setStatus(_A)
_HwVoAnalogIfFXOObjects_ObjectIdentity=ObjectIdentity
hwVoAnalogIfFXOObjects=_HwVoAnalogIfFXOObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,3,3))
_HwVoAnalogIfFXOConfigTable_Object=MibTable
hwVoAnalogIfFXOConfigTable=_HwVoAnalogIfFXOConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1))
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigTable.setStatus(_A)
_HwVoAnalogIfFXOConfigEntry_Object=MibTableRow
hwVoAnalogIfFXOConfigEntry=_HwVoAnalogIfFXOConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1))
hwVoAnalogIfFXOConfigEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigEntry.setStatus(_A)
_HwVoAnalogIfFXOConfigPortNumber_Type=Integer32
_HwVoAnalogIfFXOConfigPortNumber_Object=MibTableColumn
hwVoAnalogIfFXOConfigPortNumber=_HwVoAnalogIfFXOConfigPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,1),_HwVoAnalogIfFXOConfigPortNumber_Type())
hwVoAnalogIfFXOConfigPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigPortNumber.setStatus(_A)
class _HwVoAnalogIfFXOConfigStartMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HwVoAnalogIfFXOConfigStartMode_Type.__name__=_B
_HwVoAnalogIfFXOConfigStartMode_Object=MibTableColumn
hwVoAnalogIfFXOConfigStartMode=_HwVoAnalogIfFXOConfigStartMode_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,2),_HwVoAnalogIfFXOConfigStartMode_Type())
hwVoAnalogIfFXOConfigStartMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigStartMode.setStatus(_A)
class _HwVoAnalogIfFXOConfigAlertNumber_Type(Integer32):defaultValue=2
_HwVoAnalogIfFXOConfigAlertNumber_Type.__name__=_B
_HwVoAnalogIfFXOConfigAlertNumber_Object=MibTableColumn
hwVoAnalogIfFXOConfigAlertNumber=_HwVoAnalogIfFXOConfigAlertNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,3),_HwVoAnalogIfFXOConfigAlertNumber_Type())
hwVoAnalogIfFXOConfigAlertNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigAlertNumber.setStatus(_A)
class _HwVoAnalogIfFXOConfigArea_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('europe',1),('custom',2),('north-america',3)))
_HwVoAnalogIfFXOConfigArea_Type.__name__=_B
_HwVoAnalogIfFXOConfigArea_Object=MibTableColumn
hwVoAnalogIfFXOConfigArea=_HwVoAnalogIfFXOConfigArea_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,4),_HwVoAnalogIfFXOConfigArea_Type())
hwVoAnalogIfFXOConfigArea.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfFXOConfigArea.setStatus(_A)
class _HwVoAnalogIfFXOPreDialDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HwVoAnalogIfFXOPreDialDelay_Type.__name__=_B
_HwVoAnalogIfFXOPreDialDelay_Object=MibTableColumn
hwVoAnalogIfFXOPreDialDelay=_HwVoAnalogIfFXOPreDialDelay_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,5),_HwVoAnalogIfFXOPreDialDelay_Type())
hwVoAnalogIfFXOPreDialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfFXOPreDialDelay.setStatus(_A)
class _HwVoAnaloglfFXOConfigPortImpedance_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('impedance550r',0),('impedance600r',1),('impedance600c',2),('impedancecomplex',3)))
_HwVoAnaloglfFXOConfigPortImpedance_Type.__name__=_B
_HwVoAnaloglfFXOConfigPortImpedance_Object=MibTableColumn
hwVoAnaloglfFXOConfigPortImpedance=_HwVoAnaloglfFXOConfigPortImpedance_Object((1,3,6,1,4,1,2011,5,25,1,3,3,1,1,6),_HwVoAnaloglfFXOConfigPortImpedance_Type())
hwVoAnaloglfFXOConfigPortImpedance.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnaloglfFXOConfigPortImpedance.setStatus(_A)
_HwVoAnalogIfFXOTimerTable_Object=MibTable
hwVoAnalogIfFXOTimerTable=_HwVoAnalogIfFXOTimerTable_Object((1,3,6,1,4,1,2011,5,25,1,3,3,3))
if mibBuilder.loadTexts:hwVoAnalogIfFXOTimerTable.setStatus(_A)
_HwVoAnalogIfFXOTimerEntry_Object=MibTableRow
hwVoAnalogIfFXOTimerEntry=_HwVoAnalogIfFXOTimerEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,3,3,1))
hwVoAnalogIfFXOTimerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hwVoAnalogIfFXOTimerEntry.setStatus(_A)
_HwVoAnalogIfFXOTimerPortNumber_Type=Integer32
_HwVoAnalogIfFXOTimerPortNumber_Object=MibTableColumn
hwVoAnalogIfFXOTimerPortNumber=_HwVoAnalogIfFXOTimerPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,3,3,1,1),_HwVoAnalogIfFXOTimerPortNumber_Type())
hwVoAnalogIfFXOTimerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfFXOTimerPortNumber.setStatus(_A)
class _HwVoAnalogIfFXOTimerDtmf_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfFXOTimerDtmf_Type.__name__=_B
_HwVoAnalogIfFXOTimerDtmf_Object=MibTableColumn
hwVoAnalogIfFXOTimerDtmf=_HwVoAnalogIfFXOTimerDtmf_Object((1,3,6,1,4,1,2011,5,25,1,3,3,3,1,2),_HwVoAnalogIfFXOTimerDtmf_Type())
hwVoAnalogIfFXOTimerDtmf.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfFXOTimerDtmf.setStatus(_A)
class _HwVoAnalogIfFXOTimerDtmfInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfFXOTimerDtmfInterval_Type.__name__=_B
_HwVoAnalogIfFXOTimerDtmfInterval_Object=MibTableColumn
hwVoAnalogIfFXOTimerDtmfInterval=_HwVoAnalogIfFXOTimerDtmfInterval_Object((1,3,6,1,4,1,2011,5,25,1,3,3,3,1,3),_HwVoAnalogIfFXOTimerDtmfInterval_Type())
hwVoAnalogIfFXOTimerDtmfInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfFXOTimerDtmfInterval.setStatus(_A)
_HwVoAnalogIfEMObjects_ObjectIdentity=ObjectIdentity
hwVoAnalogIfEMObjects=_HwVoAnalogIfEMObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,3,4))
_HwVoAnalogIfEMConfigTable_Object=MibTable
hwVoAnalogIfEMConfigTable=_HwVoAnalogIfEMConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1))
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigTable.setStatus(_A)
_HwVoAnalogIfEMConfigEntry_Object=MibTableRow
hwVoAnalogIfEMConfigEntry=_HwVoAnalogIfEMConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1))
hwVoAnalogIfEMConfigEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigEntry.setStatus(_A)
_HwVoAnalogIfEMConfigPortNumber_Type=Integer32
_HwVoAnalogIfEMConfigPortNumber_Object=MibTableColumn
hwVoAnalogIfEMConfigPortNumber=_HwVoAnalogIfEMConfigPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,1),_HwVoAnalogIfEMConfigPortNumber_Type())
hwVoAnalogIfEMConfigPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigPortNumber.setStatus(_A)
class _HwVoAnalogIfEMConfigSignalMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delayDial',1),('immediateDial',2),('winkStart',3)))
_HwVoAnalogIfEMConfigSignalMode_Type.__name__=_B
_HwVoAnalogIfEMConfigSignalMode_Object=MibTableColumn
hwVoAnalogIfEMConfigSignalMode=_HwVoAnalogIfEMConfigSignalMode_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,2),_HwVoAnalogIfEMConfigSignalMode_Type())
hwVoAnalogIfEMConfigSignalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigSignalMode.setStatus(_A)
class _HwVoAnalogIfEMConfigPhyParm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoWiresOperation',1),('fourWiresOperation',2)))
_HwVoAnalogIfEMConfigPhyParm_Type.__name__=_B
_HwVoAnalogIfEMConfigPhyParm_Object=MibTableColumn
hwVoAnalogIfEMConfigPhyParm=_HwVoAnalogIfEMConfigPhyParm_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,3),_HwVoAnalogIfEMConfigPhyParm_Type())
hwVoAnalogIfEMConfigPhyParm.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigPhyParm.setStatus(_A)
class _HwVoAnalogIfEMConfigPhyType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3),('type5',5)))
_HwVoAnalogIfEMConfigPhyType_Type.__name__=_B
_HwVoAnalogIfEMConfigPhyType_Object=MibTableColumn
hwVoAnalogIfEMConfigPhyType=_HwVoAnalogIfEMConfigPhyType_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,4),_HwVoAnalogIfEMConfigPhyType_Type())
hwVoAnalogIfEMConfigPhyType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigPhyType.setStatus(_A)
class _HwVoAnalogIfEMConfigTimeoutRinging_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600),ValueRangeConstraint(65535,65535))
_HwVoAnalogIfEMConfigTimeoutRinging_Type.__name__=_B
_HwVoAnalogIfEMConfigTimeoutRinging_Object=MibTableColumn
hwVoAnalogIfEMConfigTimeoutRinging=_HwVoAnalogIfEMConfigTimeoutRinging_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,5),_HwVoAnalogIfEMConfigTimeoutRinging_Type())
hwVoAnalogIfEMConfigTimeoutRinging.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigTimeoutRinging.setStatus(_A)
class _HwVoAnalogIfEMConfigTimeoutWaitDigit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,600),ValueRangeConstraint(65535,65535))
_HwVoAnalogIfEMConfigTimeoutWaitDigit_Type.__name__=_B
_HwVoAnalogIfEMConfigTimeoutWaitDigit_Object=MibTableColumn
hwVoAnalogIfEMConfigTimeoutWaitDigit=_HwVoAnalogIfEMConfigTimeoutWaitDigit_Object((1,3,6,1,4,1,2011,5,25,1,3,4,1,1,6),_HwVoAnalogIfEMConfigTimeoutWaitDigit_Type())
hwVoAnalogIfEMConfigTimeoutWaitDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMConfigTimeoutWaitDigit.setStatus(_A)
_HwVoAnalogIfEMTimerTable_Object=MibTable
hwVoAnalogIfEMTimerTable=_HwVoAnalogIfEMTimerTable_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3))
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerTable.setStatus(_A)
_HwVoAnalogIfEMTimerEntry_Object=MibTableRow
hwVoAnalogIfEMTimerEntry=_HwVoAnalogIfEMTimerEntry_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1))
hwVoAnalogIfEMTimerEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerEntry.setStatus(_A)
_HwVoAnalogIfEMTimerPortNumber_Type=Integer32
_HwVoAnalogIfEMTimerPortNumber_Object=MibTableColumn
hwVoAnalogIfEMTimerPortNumber=_HwVoAnalogIfEMTimerPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,1),_HwVoAnalogIfEMTimerPortNumber_Type())
hwVoAnalogIfEMTimerPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerPortNumber.setStatus(_A)
class _HwVoAnalogIfEMTimerDtmf_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfEMTimerDtmf_Type.__name__=_B
_HwVoAnalogIfEMTimerDtmf_Object=MibTableColumn
hwVoAnalogIfEMTimerDtmf=_HwVoAnalogIfEMTimerDtmf_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,2),_HwVoAnalogIfEMTimerDtmf_Type())
hwVoAnalogIfEMTimerDtmf.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerDtmf.setStatus(_A)
class _HwVoAnalogIfEMTimerDtmfInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_HwVoAnalogIfEMTimerDtmfInterval_Type.__name__=_B
_HwVoAnalogIfEMTimerDtmfInterval_Object=MibTableColumn
hwVoAnalogIfEMTimerDtmfInterval=_HwVoAnalogIfEMTimerDtmfInterval_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,3),_HwVoAnalogIfEMTimerDtmfInterval_Type())
hwVoAnalogIfEMTimerDtmfInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerDtmfInterval.setStatus(_A)
class _HwVoAnalogIfEMTimerCallInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,2000))
_HwVoAnalogIfEMTimerCallInterval_Type.__name__=_B
_HwVoAnalogIfEMTimerCallInterval_Object=MibTableColumn
hwVoAnalogIfEMTimerCallInterval=_HwVoAnalogIfEMTimerCallInterval_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,4),_HwVoAnalogIfEMTimerCallInterval_Type())
hwVoAnalogIfEMTimerCallInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerCallInterval.setStatus(_A)
class _HwVoAnalogIfEMTimerSendWink_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoAnalogIfEMTimerSendWink_Type.__name__=_B
_HwVoAnalogIfEMTimerSendWink_Object=MibTableColumn
hwVoAnalogIfEMTimerSendWink=_HwVoAnalogIfEMTimerSendWink_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,5),_HwVoAnalogIfEMTimerSendWink_Type())
hwVoAnalogIfEMTimerSendWink.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerSendWink.setStatus(_A)
class _HwVoAnalogIfEMTimerWinkRising_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoAnalogIfEMTimerWinkRising_Type.__name__=_B
_HwVoAnalogIfEMTimerWinkRising_Object=MibTableColumn
hwVoAnalogIfEMTimerWinkRising=_HwVoAnalogIfEMTimerWinkRising_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,6),_HwVoAnalogIfEMTimerWinkRising_Type())
hwVoAnalogIfEMTimerWinkRising.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerWinkRising.setStatus(_A)
class _HwVoAnalogIfEMTimerWinkHold_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_HwVoAnalogIfEMTimerWinkHold_Type.__name__=_B
_HwVoAnalogIfEMTimerWinkHold_Object=MibTableColumn
hwVoAnalogIfEMTimerWinkHold=_HwVoAnalogIfEMTimerWinkHold_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,7),_HwVoAnalogIfEMTimerWinkHold_Type())
hwVoAnalogIfEMTimerWinkHold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerWinkHold.setStatus(_A)
class _HwVoAnalogIfEMTimerDialoutDelay_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,5000))
_HwVoAnalogIfEMTimerDialoutDelay_Type.__name__=_B
_HwVoAnalogIfEMTimerDialoutDelay_Object=MibTableColumn
hwVoAnalogIfEMTimerDialoutDelay=_HwVoAnalogIfEMTimerDialoutDelay_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,8),_HwVoAnalogIfEMTimerDialoutDelay_Type())
hwVoAnalogIfEMTimerDialoutDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerDialoutDelay.setStatus(_A)
class _HwVoAnalogIfEMTimerRising_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_HwVoAnalogIfEMTimerRising_Type.__name__=_B
_HwVoAnalogIfEMTimerRising_Object=MibTableColumn
hwVoAnalogIfEMTimerRising=_HwVoAnalogIfEMTimerRising_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,9),_HwVoAnalogIfEMTimerRising_Type())
hwVoAnalogIfEMTimerRising.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerRising.setStatus(_A)
class _HwVoAnalogIfEMTimerHold_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HwVoAnalogIfEMTimerHold_Type.__name__=_B
_HwVoAnalogIfEMTimerHold_Object=MibTableColumn
hwVoAnalogIfEMTimerHold=_HwVoAnalogIfEMTimerHold_Object((1,3,6,1,4,1,2011,5,25,1,3,4,3,1,10),_HwVoAnalogIfEMTimerHold_Type())
hwVoAnalogIfEMTimerHold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwVoAnalogIfEMTimerHold.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwVoiceAnalogInterfaceMIB':hwVoiceAnalogInterfaceMIB,'hwVoAnalogIfCommonObjects':hwVoAnalogIfCommonObjects,'hwVoAnalogIfCommonConfigTable':hwVoAnalogIfCommonConfigTable,'hwVoAnalogIfCommonConfigEntry':hwVoAnalogIfCommonConfigEntry,_F:hwVoAnalogIfConfigPortNumber,'hwVoAnalogIfConfigPortType':hwVoAnalogIfConfigPortType,'hwVoAnaloglfConfigPortImpedance':hwVoAnaloglfConfigPortImpedance,'hwVoAnalogIfConfigInitialDigitTimeOut':hwVoAnalogIfConfigInitialDigitTimeOut,'hwVoAnalogIfConfigInterDigitTimeOut':hwVoAnalogIfConfigInterDigitTimeOut,'hwVoAnalogIfConfigCallDisconnect':hwVoAnalogIfConfigCallDisconnect,'hwVoAnalogIfFXSObjects':hwVoAnalogIfFXSObjects,'hwVoAnalogIfFXSConfigTable':hwVoAnalogIfFXSConfigTable,'hwVoAnalogIfFXSConfigEntry':hwVoAnalogIfFXSConfigEntry,_G:hwVoAnalogIfFXSConfigPortNumber,'hwVoAnalogIfFXSConfigStartMode':hwVoAnalogIfFXSConfigStartMode,'hwVoAnalogIfFXSTimerTable':hwVoAnalogIfFXSTimerTable,'hwVoAnalogIfFXSTimerEntry':hwVoAnalogIfFXSTimerEntry,_J:hwVoAnalogIfFXSTimerPortNumber,'hwVoAnalogIfFXSTimerDtmf':hwVoAnalogIfFXSTimerDtmf,'hwVoAnalogIfFXSTimerDtmfInterval':hwVoAnalogIfFXSTimerDtmfInterval,'hwVoAnalogIfFXOObjects':hwVoAnalogIfFXOObjects,'hwVoAnalogIfFXOConfigTable':hwVoAnalogIfFXOConfigTable,'hwVoAnalogIfFXOConfigEntry':hwVoAnalogIfFXOConfigEntry,_K:hwVoAnalogIfFXOConfigPortNumber,'hwVoAnalogIfFXOConfigStartMode':hwVoAnalogIfFXOConfigStartMode,'hwVoAnalogIfFXOConfigAlertNumber':hwVoAnalogIfFXOConfigAlertNumber,'hwVoAnalogIfFXOConfigArea':hwVoAnalogIfFXOConfigArea,'hwVoAnalogIfFXOPreDialDelay':hwVoAnalogIfFXOPreDialDelay,'hwVoAnaloglfFXOConfigPortImpedance':hwVoAnaloglfFXOConfigPortImpedance,'hwVoAnalogIfFXOTimerTable':hwVoAnalogIfFXOTimerTable,'hwVoAnalogIfFXOTimerEntry':hwVoAnalogIfFXOTimerEntry,_L:hwVoAnalogIfFXOTimerPortNumber,'hwVoAnalogIfFXOTimerDtmf':hwVoAnalogIfFXOTimerDtmf,'hwVoAnalogIfFXOTimerDtmfInterval':hwVoAnalogIfFXOTimerDtmfInterval,'hwVoAnalogIfEMObjects':hwVoAnalogIfEMObjects,'hwVoAnalogIfEMConfigTable':hwVoAnalogIfEMConfigTable,'hwVoAnalogIfEMConfigEntry':hwVoAnalogIfEMConfigEntry,_M:hwVoAnalogIfEMConfigPortNumber,'hwVoAnalogIfEMConfigSignalMode':hwVoAnalogIfEMConfigSignalMode,'hwVoAnalogIfEMConfigPhyParm':hwVoAnalogIfEMConfigPhyParm,'hwVoAnalogIfEMConfigPhyType':hwVoAnalogIfEMConfigPhyType,'hwVoAnalogIfEMConfigTimeoutRinging':hwVoAnalogIfEMConfigTimeoutRinging,'hwVoAnalogIfEMConfigTimeoutWaitDigit':hwVoAnalogIfEMConfigTimeoutWaitDigit,'hwVoAnalogIfEMTimerTable':hwVoAnalogIfEMTimerTable,'hwVoAnalogIfEMTimerEntry':hwVoAnalogIfEMTimerEntry,_N:hwVoAnalogIfEMTimerPortNumber,'hwVoAnalogIfEMTimerDtmf':hwVoAnalogIfEMTimerDtmf,'hwVoAnalogIfEMTimerDtmfInterval':hwVoAnalogIfEMTimerDtmfInterval,'hwVoAnalogIfEMTimerCallInterval':hwVoAnalogIfEMTimerCallInterval,'hwVoAnalogIfEMTimerSendWink':hwVoAnalogIfEMTimerSendWink,'hwVoAnalogIfEMTimerWinkRising':hwVoAnalogIfEMTimerWinkRising,'hwVoAnalogIfEMTimerWinkHold':hwVoAnalogIfEMTimerWinkHold,'hwVoAnalogIfEMTimerDialoutDelay':hwVoAnalogIfEMTimerDialoutDelay,'hwVoAnalogIfEMTimerRising':hwVoAnalogIfEMTimerRising,'hwVoAnalogIfEMTimerHold':hwVoAnalogIfEMTimerHold})