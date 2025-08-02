_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifEntry,ifIndex=mibBuilder.importSymbols(_C,'ifEntry',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cTransceiver=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,70))
if mibBuilder.loadTexts:h3cTransceiver.setRevisions(('2009-12-29 16:50',))
_H3cTransceiverInfoAdm_ObjectIdentity=ObjectIdentity
h3cTransceiverInfoAdm=_H3cTransceiverInfoAdm_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,70,1))
_H3cTransceiverInfoTable_Object=MibTable
h3cTransceiverInfoTable=_H3cTransceiverInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1))
if mibBuilder.loadTexts:h3cTransceiverInfoTable.setStatus(_A)
_H3cTransceiverInfoEntry_Object=MibTableRow
h3cTransceiverInfoEntry=_H3cTransceiverInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1))
h3cTransceiverInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cTransceiverInfoEntry.setStatus(_A)
_H3cTransceiverHardwareType_Type=OctetString
_H3cTransceiverHardwareType_Object=MibTableColumn
h3cTransceiverHardwareType=_H3cTransceiverHardwareType_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,1),_H3cTransceiverHardwareType_Type())
h3cTransceiverHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverHardwareType.setStatus(_A)
_H3cTransceiverType_Type=OctetString
_H3cTransceiverType_Object=MibTableColumn
h3cTransceiverType=_H3cTransceiverType_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,2),_H3cTransceiverType_Type())
h3cTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverType.setStatus(_A)
_H3cTransceiverWaveLength_Type=Integer32
_H3cTransceiverWaveLength_Object=MibTableColumn
h3cTransceiverWaveLength=_H3cTransceiverWaveLength_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,3),_H3cTransceiverWaveLength_Type())
h3cTransceiverWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverWaveLength.setStatus(_A)
_H3cTransceiverVendorName_Type=OctetString
_H3cTransceiverVendorName_Object=MibTableColumn
h3cTransceiverVendorName=_H3cTransceiverVendorName_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,4),_H3cTransceiverVendorName_Type())
h3cTransceiverVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVendorName.setStatus(_A)
_H3cTransceiverSerialNumber_Type=OctetString
_H3cTransceiverSerialNumber_Object=MibTableColumn
h3cTransceiverSerialNumber=_H3cTransceiverSerialNumber_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,5),_H3cTransceiverSerialNumber_Type())
h3cTransceiverSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverSerialNumber.setStatus(_A)
class _H3cTransceiverFiberDiameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,65535)));namedValues=NamedValues(*(('fiber9',1),('fiber50',2),('fiber625',3),('copper',4),('unknown',65535)))
_H3cTransceiverFiberDiameterType_Type.__name__=_E
_H3cTransceiverFiberDiameterType_Object=MibTableColumn
h3cTransceiverFiberDiameterType=_H3cTransceiverFiberDiameterType_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,6),_H3cTransceiverFiberDiameterType_Type())
h3cTransceiverFiberDiameterType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverFiberDiameterType.setStatus(_A)
_H3cTransceiverTransferDistance_Type=Integer32
_H3cTransceiverTransferDistance_Object=MibTableColumn
h3cTransceiverTransferDistance=_H3cTransceiverTransferDistance_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,7),_H3cTransceiverTransferDistance_Type())
h3cTransceiverTransferDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTransferDistance.setStatus(_A)
_H3cTransceiverDiagnostic_Type=TruthValue
_H3cTransceiverDiagnostic_Object=MibTableColumn
h3cTransceiverDiagnostic=_H3cTransceiverDiagnostic_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,8),_H3cTransceiverDiagnostic_Type())
h3cTransceiverDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverDiagnostic.setStatus(_A)
_H3cTransceiverCurTXPower_Type=Integer32
_H3cTransceiverCurTXPower_Object=MibTableColumn
h3cTransceiverCurTXPower=_H3cTransceiverCurTXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,9),_H3cTransceiverCurTXPower_Type())
h3cTransceiverCurTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurTXPower.setStatus(_A)
_H3cTransceiverMaxTXPower_Type=Integer32
_H3cTransceiverMaxTXPower_Object=MibTableColumn
h3cTransceiverMaxTXPower=_H3cTransceiverMaxTXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,10),_H3cTransceiverMaxTXPower_Type())
h3cTransceiverMaxTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMaxTXPower.setStatus(_A)
_H3cTransceiverMinTXPower_Type=Integer32
_H3cTransceiverMinTXPower_Object=MibTableColumn
h3cTransceiverMinTXPower=_H3cTransceiverMinTXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,11),_H3cTransceiverMinTXPower_Type())
h3cTransceiverMinTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMinTXPower.setStatus(_A)
_H3cTransceiverCurRXPower_Type=Integer32
_H3cTransceiverCurRXPower_Object=MibTableColumn
h3cTransceiverCurRXPower=_H3cTransceiverCurRXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,12),_H3cTransceiverCurRXPower_Type())
h3cTransceiverCurRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurRXPower.setStatus(_A)
_H3cTransceiverMaxRXPower_Type=Integer32
_H3cTransceiverMaxRXPower_Object=MibTableColumn
h3cTransceiverMaxRXPower=_H3cTransceiverMaxRXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,13),_H3cTransceiverMaxRXPower_Type())
h3cTransceiverMaxRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMaxRXPower.setStatus(_A)
_H3cTransceiverMinRXPower_Type=Integer32
_H3cTransceiverMinRXPower_Object=MibTableColumn
h3cTransceiverMinRXPower=_H3cTransceiverMinRXPower_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,14),_H3cTransceiverMinRXPower_Type())
h3cTransceiverMinRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMinRXPower.setStatus(_A)
_H3cTransceiverTemperature_Type=Integer32
_H3cTransceiverTemperature_Object=MibTableColumn
h3cTransceiverTemperature=_H3cTransceiverTemperature_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,15),_H3cTransceiverTemperature_Type())
h3cTransceiverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTemperature.setStatus(_A)
_H3cTransceiverVoltage_Type=Integer32
_H3cTransceiverVoltage_Object=MibTableColumn
h3cTransceiverVoltage=_H3cTransceiverVoltage_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,16),_H3cTransceiverVoltage_Type())
h3cTransceiverVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVoltage.setStatus(_A)
_H3cTransceiverBiasCurrent_Type=Integer32
_H3cTransceiverBiasCurrent_Object=MibTableColumn
h3cTransceiverBiasCurrent=_H3cTransceiverBiasCurrent_Object((1,3,6,1,4,1,43,45,1,10,2,70,1,1,1,17),_H3cTransceiverBiasCurrent_Type())
h3cTransceiverBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasCurrent.setStatus(_A)
mibBuilder.exportSymbols('A3COM-HUAWEI-TRANSCEIVER-INFO-MIB',**{'h3cTransceiver':h3cTransceiver,'h3cTransceiverInfoAdm':h3cTransceiverInfoAdm,'h3cTransceiverInfoTable':h3cTransceiverInfoTable,'h3cTransceiverInfoEntry':h3cTransceiverInfoEntry,'h3cTransceiverHardwareType':h3cTransceiverHardwareType,'h3cTransceiverType':h3cTransceiverType,'h3cTransceiverWaveLength':h3cTransceiverWaveLength,'h3cTransceiverVendorName':h3cTransceiverVendorName,'h3cTransceiverSerialNumber':h3cTransceiverSerialNumber,'h3cTransceiverFiberDiameterType':h3cTransceiverFiberDiameterType,'h3cTransceiverTransferDistance':h3cTransceiverTransferDistance,'h3cTransceiverDiagnostic':h3cTransceiverDiagnostic,'h3cTransceiverCurTXPower':h3cTransceiverCurTXPower,'h3cTransceiverMaxTXPower':h3cTransceiverMaxTXPower,'h3cTransceiverMinTXPower':h3cTransceiverMinTXPower,'h3cTransceiverCurRXPower':h3cTransceiverCurRXPower,'h3cTransceiverMaxRXPower':h3cTransceiverMaxRXPower,'h3cTransceiverMinRXPower':h3cTransceiverMinRXPower,'h3cTransceiverTemperature':h3cTransceiverTemperature,'h3cTransceiverVoltage':h3cTransceiverVoltage,'h3cTransceiverBiasCurrent':h3cTransceiverBiasCurrent})