_S='rLIRLinkFailureType'
_R='rLIRConnectedPortWwn'
_Q='rLIRIncidentPortWwn'
_P='switchRNIDIndex'
_O='DisplayString'
_N='Integer32'
_M='lIRRListenerPortWWN'
_L='nodeRNIDConnectedPortWWN'
_K='nodeRNIDIncidentPortWWN'
_J='rLIRIndex'
_I='lIRRListenerPID'
_H='lIRRIndex'
_G='nodeRNIDIndex'
_F='ficonPort'
_E='ficonSlot'
_D='nodeVfId'
_C='LINK-INCIDENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fcSwitch,=mibBuilder.importSymbols('Brocade-REG-MIB','fcSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
linkIncidentMIB=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,50))
if mibBuilder.loadTexts:linkIncidentMIB.setRevisions(('2003-07-11 00:00','2012-06-04 00:00'))
class FcPortID(TextualConvention,OctetString):status=_A;displayHint='x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class RLIRLinkFailureType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bitErrorRate',2),('lossOfSignal',3),('nOSRecognized',4),('primitiveSequenceTimeout',5),('invalidSeqForPortState',6),('loopInitializationTimeout',7),('lossOfSignalInLoopInit',8)))
class LinkWwn(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('n-port',1),('nl-port',2),('e-port',3)))
class LinkFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ficon',1),('common',2)))
class RegType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conditional',1),('unconditional',2)))
class LIRRProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fcp',1),('sb2',2)))
class RNIDTagType(TextualConvention,OctetString):status=_A;displayHint='x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class RNIDFlags(TextualConvention,OctetString):status=_A;displayHint='x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class RNIDType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class RNIDModel(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class RNIDManufacturer(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class RNIDManufacturerPlant(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class RNIDSequenceNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
class RNIDParams(TextualConvention,OctetString):status=_A;displayHint='x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_FiconRNID_ObjectIdentity=ObjectIdentity
ficonRNID=_FiconRNID_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,50,2))
if mibBuilder.loadTexts:ficonRNID.setStatus(_A)
_NodeRNIDTableNumEntries_Type=Integer32
_NodeRNIDTableNumEntries_Object=MibScalar
nodeRNIDTableNumEntries=_NodeRNIDTableNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,50,2,1),_NodeRNIDTableNumEntries_Type())
nodeRNIDTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDTableNumEntries.setStatus(_A)
_NodeRNIDTable_Object=MibTable
nodeRNIDTable=_NodeRNIDTable_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2))
if mibBuilder.loadTexts:nodeRNIDTable.setStatus(_A)
_NodeRNIDEntry_Object=MibTableRow
nodeRNIDEntry=_NodeRNIDEntry_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1))
nodeRNIDEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:nodeRNIDEntry.setStatus(_A)
_NodeRNIDIndex_Type=Integer32
_NodeRNIDIndex_Object=MibTableColumn
nodeRNIDIndex=_NodeRNIDIndex_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,1),_NodeRNIDIndex_Type())
nodeRNIDIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDIndex.setStatus(_A)
_NodeRNIDIncidentPortWWN_Type=LinkWwn
_NodeRNIDIncidentPortWWN_Object=MibTableColumn
nodeRNIDIncidentPortWWN=_NodeRNIDIncidentPortWWN_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,2),_NodeRNIDIncidentPortWWN_Type())
nodeRNIDIncidentPortWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDIncidentPortWWN.setStatus(_A)
_NodeRNIDPID_Type=FcPortID
_NodeRNIDPID_Object=MibTableColumn
nodeRNIDPID=_NodeRNIDPID_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,3),_NodeRNIDPID_Type())
nodeRNIDPID.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDPID.setStatus(_A)
_NodeRNIDFlags_Type=RNIDFlags
_NodeRNIDFlags_Object=MibTableColumn
nodeRNIDFlags=_NodeRNIDFlags_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,4),_NodeRNIDFlags_Type())
nodeRNIDFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDFlags.setStatus(_A)
_NodeRNIDType_Type=RNIDType
_NodeRNIDType_Object=MibTableColumn
nodeRNIDType=_NodeRNIDType_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,5),_NodeRNIDType_Type())
nodeRNIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDType.setStatus(_A)
_NodeRNIDModel_Type=RNIDModel
_NodeRNIDModel_Object=MibTableColumn
nodeRNIDModel=_NodeRNIDModel_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,6),_NodeRNIDModel_Type())
nodeRNIDModel.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDModel.setStatus(_A)
_NodeRNIDManufacturer_Type=RNIDManufacturer
_NodeRNIDManufacturer_Object=MibTableColumn
nodeRNIDManufacturer=_NodeRNIDManufacturer_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,7),_NodeRNIDManufacturer_Type())
nodeRNIDManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDManufacturer.setStatus(_A)
_NodeRNIDManufacturerPlant_Type=RNIDManufacturerPlant
_NodeRNIDManufacturerPlant_Object=MibTableColumn
nodeRNIDManufacturerPlant=_NodeRNIDManufacturerPlant_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,8),_NodeRNIDManufacturerPlant_Type())
nodeRNIDManufacturerPlant.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDManufacturerPlant.setStatus(_A)
_NodeRNIDSequenceNumber_Type=RNIDSequenceNumber
_NodeRNIDSequenceNumber_Object=MibTableColumn
nodeRNIDSequenceNumber=_NodeRNIDSequenceNumber_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,9),_NodeRNIDSequenceNumber_Type())
nodeRNIDSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDSequenceNumber.setStatus(_A)
_NodeRNIDConnectedPortWWN_Type=LinkWwn
_NodeRNIDConnectedPortWWN_Object=MibTableColumn
nodeRNIDConnectedPortWWN=_NodeRNIDConnectedPortWWN_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,10),_NodeRNIDConnectedPortWWN_Type())
nodeRNIDConnectedPortWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDConnectedPortWWN.setStatus(_A)
_NodeRNIDPortType_Type=PortType
_NodeRNIDPortType_Object=MibTableColumn
nodeRNIDPortType=_NodeRNIDPortType_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,11),_NodeRNIDPortType_Type())
nodeRNIDPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDPortType.setStatus(_A)
_NodeRNIDFormat_Type=LinkFormat
_NodeRNIDFormat_Object=MibTableColumn
nodeRNIDFormat=_NodeRNIDFormat_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,12),_NodeRNIDFormat_Type())
nodeRNIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDFormat.setStatus(_A)
_NodeRNIDTag_Type=RNIDTagType
_NodeRNIDTag_Object=MibTableColumn
nodeRNIDTag=_NodeRNIDTag_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,13),_NodeRNIDTag_Type())
nodeRNIDTag.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDTag.setStatus(_A)
_NodeRNIDParams_Type=RNIDParams
_NodeRNIDParams_Object=MibTableColumn
nodeRNIDParams=_NodeRNIDParams_Object((1,3,6,1,4,1,1588,2,1,1,50,2,2,1,14),_NodeRNIDParams_Type())
nodeRNIDParams.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeRNIDParams.setStatus(_A)
_SwitchRNIDTableNumEntries_Type=Integer32
_SwitchRNIDTableNumEntries_Object=MibScalar
switchRNIDTableNumEntries=_SwitchRNIDTableNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,50,2,3),_SwitchRNIDTableNumEntries_Type())
switchRNIDTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDTableNumEntries.setStatus(_A)
_SwitchRNIDTable_Object=MibTable
switchRNIDTable=_SwitchRNIDTable_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4))
if mibBuilder.loadTexts:switchRNIDTable.setStatus(_A)
_SwitchRNIDEntry_Object=MibTableRow
switchRNIDEntry=_SwitchRNIDEntry_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1))
switchRNIDEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:switchRNIDEntry.setStatus(_A)
_SwitchRNIDIndex_Type=Integer32
_SwitchRNIDIndex_Object=MibTableColumn
switchRNIDIndex=_SwitchRNIDIndex_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,1),_SwitchRNIDIndex_Type())
switchRNIDIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDIndex.setStatus(_A)
_SwitchRNIDSwitchWWN_Type=LinkWwn
_SwitchRNIDSwitchWWN_Object=MibTableColumn
switchRNIDSwitchWWN=_SwitchRNIDSwitchWWN_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,2),_SwitchRNIDSwitchWWN_Type())
switchRNIDSwitchWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDSwitchWWN.setStatus(_A)
_SwitchRNIDFlags_Type=RNIDFlags
_SwitchRNIDFlags_Object=MibTableColumn
switchRNIDFlags=_SwitchRNIDFlags_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,3),_SwitchRNIDFlags_Type())
switchRNIDFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDFlags.setStatus(_A)
_SwitchRNIDType_Type=RNIDType
_SwitchRNIDType_Object=MibTableColumn
switchRNIDType=_SwitchRNIDType_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,4),_SwitchRNIDType_Type())
switchRNIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDType.setStatus(_A)
_SwitchRNIDModel_Type=RNIDModel
_SwitchRNIDModel_Object=MibTableColumn
switchRNIDModel=_SwitchRNIDModel_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,5),_SwitchRNIDModel_Type())
switchRNIDModel.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDModel.setStatus(_A)
_SwitchRNIDManufacturer_Type=RNIDManufacturer
_SwitchRNIDManufacturer_Object=MibTableColumn
switchRNIDManufacturer=_SwitchRNIDManufacturer_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,6),_SwitchRNIDManufacturer_Type())
switchRNIDManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDManufacturer.setStatus(_A)
_SwitchRNIDManufacturerPlant_Type=RNIDManufacturerPlant
_SwitchRNIDManufacturerPlant_Object=MibTableColumn
switchRNIDManufacturerPlant=_SwitchRNIDManufacturerPlant_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,7),_SwitchRNIDManufacturerPlant_Type())
switchRNIDManufacturerPlant.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDManufacturerPlant.setStatus(_A)
_SwitchRNIDSequenceNumber_Type=RNIDSequenceNumber
_SwitchRNIDSequenceNumber_Object=MibTableColumn
switchRNIDSequenceNumber=_SwitchRNIDSequenceNumber_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,8),_SwitchRNIDSequenceNumber_Type())
switchRNIDSequenceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDSequenceNumber.setStatus(_A)
_SwitchRNIDTag_Type=RNIDTagType
_SwitchRNIDTag_Object=MibTableColumn
switchRNIDTag=_SwitchRNIDTag_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,9),_SwitchRNIDTag_Type())
switchRNIDTag.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDTag.setStatus(_A)
_SwitchRNIDParams_Type=RNIDParams
_SwitchRNIDParams_Object=MibTableColumn
switchRNIDParams=_SwitchRNIDParams_Object((1,3,6,1,4,1,1588,2,1,1,50,2,4,1,10),_SwitchRNIDParams_Type())
switchRNIDParams.setMaxAccess(_B)
if mibBuilder.loadTexts:switchRNIDParams.setStatus(_A)
class _NodeVfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NodeVfId_Type.__name__=_N
_NodeVfId_Object=MibScalar
nodeVfId=_NodeVfId_Object((1,3,6,1,4,1,1588,2,1,1,50,2,5),_NodeVfId_Type())
nodeVfId.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeVfId.setStatus(_A)
_FiconSlot_Type=Integer32
_FiconSlot_Object=MibScalar
ficonSlot=_FiconSlot_Object((1,3,6,1,4,1,1588,2,1,1,50,2,6),_FiconSlot_Type())
ficonSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ficonSlot.setStatus(_A)
_FiconPort_Type=Integer32
_FiconPort_Object=MibScalar
ficonPort=_FiconPort_Object((1,3,6,1,4,1,1588,2,1,1,50,2,7),_FiconPort_Type())
ficonPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ficonPort.setStatus(_A)
_FiconLIRR_ObjectIdentity=ObjectIdentity
ficonLIRR=_FiconLIRR_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,50,3))
if mibBuilder.loadTexts:ficonLIRR.setStatus(_A)
_LIRRTableNumEntries_Type=Integer32
_LIRRTableNumEntries_Object=MibScalar
lIRRTableNumEntries=_LIRRTableNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,50,3,1),_LIRRTableNumEntries_Type())
lIRRTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRTableNumEntries.setStatus(_A)
_LIRRTable_Object=MibTable
lIRRTable=_LIRRTable_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2))
if mibBuilder.loadTexts:lIRRTable.setStatus(_A)
_LIRREntry_Object=MibTableRow
lIRREntry=_LIRREntry_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1))
lIRREntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:lIRREntry.setStatus(_A)
_LIRRIndex_Type=Integer32
_LIRRIndex_Object=MibTableColumn
lIRRIndex=_LIRRIndex_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,1),_LIRRIndex_Type())
lIRRIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRIndex.setStatus(_A)
_LIRRListenerPortWWN_Type=LinkWwn
_LIRRListenerPortWWN_Object=MibTableColumn
lIRRListenerPortWWN=_LIRRListenerPortWWN_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,2),_LIRRListenerPortWWN_Type())
lIRRListenerPortWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRListenerPortWWN.setStatus(_A)
_LIRRListenerPID_Type=FcPortID
_LIRRListenerPID_Object=MibTableColumn
lIRRListenerPID=_LIRRListenerPID_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,3),_LIRRListenerPID_Type())
lIRRListenerPID.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRListenerPID.setStatus(_A)
_LIRRRegType_Type=RegType
_LIRRRegType_Object=MibTableColumn
lIRRRegType=_LIRRRegType_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,4),_LIRRRegType_Type())
lIRRRegType.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRRegType.setStatus(_A)
_LIRRProtocol_Type=LIRRProtocol
_LIRRProtocol_Object=MibTableColumn
lIRRProtocol=_LIRRProtocol_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,5),_LIRRProtocol_Type())
lIRRProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRProtocol.setStatus(_A)
_LIRRPortType_Type=PortType
_LIRRPortType_Object=MibTableColumn
lIRRPortType=_LIRRPortType_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,6),_LIRRPortType_Type())
lIRRPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRPortType.setStatus(_A)
_LIRRFormat_Type=LinkFormat
_LIRRFormat_Object=MibTableColumn
lIRRFormat=_LIRRFormat_Object((1,3,6,1,4,1,1588,2,1,1,50,3,2,1,7),_LIRRFormat_Type())
lIRRFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:lIRRFormat.setStatus(_A)
_FiconRLIR_ObjectIdentity=ObjectIdentity
ficonRLIR=_FiconRLIR_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,50,4))
if mibBuilder.loadTexts:ficonRLIR.setStatus(_A)
_RLIRTableNumEntries_Type=Integer32
_RLIRTableNumEntries_Object=MibScalar
rLIRTableNumEntries=_RLIRTableNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,50,4,1),_RLIRTableNumEntries_Type())
rLIRTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRTableNumEntries.setStatus(_A)
_RLIRTable_Object=MibTable
rLIRTable=_RLIRTable_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2))
if mibBuilder.loadTexts:rLIRTable.setStatus(_A)
_RLIREntry_Object=MibTableRow
rLIREntry=_RLIREntry_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1))
rLIREntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:rLIREntry.setStatus(_A)
_RLIRIndex_Type=Integer32
_RLIRIndex_Object=MibTableColumn
rLIRIndex=_RLIRIndex_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,1),_RLIRIndex_Type())
rLIRIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIndex.setStatus(_A)
_RLIRIncidentPortWwn_Type=LinkWwn
_RLIRIncidentPortWwn_Object=MibTableColumn
rLIRIncidentPortWwn=_RLIRIncidentPortWwn_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,2),_RLIRIncidentPortWwn_Type())
rLIRIncidentPortWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIncidentPortWwn.setStatus(_A)
_RLIRIncidentNodeWwn_Type=LinkWwn
_RLIRIncidentNodeWwn_Object=MibTableColumn
rLIRIncidentNodeWwn=_RLIRIncidentNodeWwn_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,3),_RLIRIncidentNodeWwn_Type())
rLIRIncidentNodeWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIncidentNodeWwn.setStatus(_A)
_RLIRIncidentPortType_Type=PortType
_RLIRIncidentPortType_Object=MibTableColumn
rLIRIncidentPortType=_RLIRIncidentPortType_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,5),_RLIRIncidentPortType_Type())
rLIRIncidentPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIncidentPortType.setStatus(_A)
_RLIRIncidentPID_Type=FcPortID
_RLIRIncidentPID_Object=MibTableColumn
rLIRIncidentPID=_RLIRIncidentPID_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,6),_RLIRIncidentPID_Type())
rLIRIncidentPID.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIncidentPID.setStatus(_A)
_RLIRIncidentPortNumber_Type=Integer32
_RLIRIncidentPortNumber_Object=MibTableColumn
rLIRIncidentPortNumber=_RLIRIncidentPortNumber_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,7),_RLIRIncidentPortNumber_Type())
rLIRIncidentPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRIncidentPortNumber.setStatus(_A)
_RLIRConnectedPortWwn_Type=LinkWwn
_RLIRConnectedPortWwn_Object=MibTableColumn
rLIRConnectedPortWwn=_RLIRConnectedPortWwn_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,8),_RLIRConnectedPortWwn_Type())
rLIRConnectedPortWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRConnectedPortWwn.setStatus(_A)
_RLIRConnectedNodeWwn_Type=LinkWwn
_RLIRConnectedNodeWwn_Object=MibTableColumn
rLIRConnectedNodeWwn=_RLIRConnectedNodeWwn_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,9),_RLIRConnectedNodeWwn_Type())
rLIRConnectedNodeWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRConnectedNodeWwn.setStatus(_A)
_RLIRFabricWwn_Type=LinkWwn
_RLIRFabricWwn_Object=MibTableColumn
rLIRFabricWwn=_RLIRFabricWwn_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,10),_RLIRFabricWwn_Type())
rLIRFabricWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRFabricWwn.setStatus(_A)
_RLIRLinkFailureType_Type=RLIRLinkFailureType
_RLIRLinkFailureType_Object=MibTableColumn
rLIRLinkFailureType=_RLIRLinkFailureType_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,11),_RLIRLinkFailureType_Type())
rLIRLinkFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRLinkFailureType.setStatus(_A)
class _RLIRTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RLIRTimeStamp_Type.__name__=_O
_RLIRTimeStamp_Object=MibTableColumn
rLIRTimeStamp=_RLIRTimeStamp_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,12),_RLIRTimeStamp_Type())
rLIRTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRTimeStamp.setStatus(_A)
_RLIRFormat_Type=LinkFormat
_RLIRFormat_Object=MibTableColumn
rLIRFormat=_RLIRFormat_Object((1,3,6,1,4,1,1588,2,1,1,50,4,2,1,13),_RLIRFormat_Type())
rLIRFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:rLIRFormat.setStatus(_A)
_LinkIncidentMIBTraps_ObjectIdentity=ObjectIdentity
linkIncidentMIBTraps=_LinkIncidentMIBTraps_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,50,21))
if mibBuilder.loadTexts:linkIncidentMIBTraps.setStatus(_A)
_LinkIncidentMIBTrapPrefix_ObjectIdentity=ObjectIdentity
linkIncidentMIBTrapPrefix=_LinkIncidentMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,50,21,0))
if mibBuilder.loadTexts:linkIncidentMIBTrapPrefix.setStatus(_A)
linkRNIDDeviceRegistration=NotificationType((1,3,6,1,4,1,1588,2,1,1,50,21,0,1))
linkRNIDDeviceRegistration.setObjects(*((_C,_G),(_C,_K),(_C,_L),(_C,_D),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:linkRNIDDeviceRegistration.setStatus(_A)
linkRNIDDeviceDeRegistration=NotificationType((1,3,6,1,4,1,1588,2,1,1,50,21,0,2))
linkRNIDDeviceDeRegistration.setObjects(*((_C,_G),(_C,_K),(_C,_L),(_C,_D),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:linkRNIDDeviceDeRegistration.setStatus(_A)
linkLIRRListenerAdded=NotificationType((1,3,6,1,4,1,1588,2,1,1,50,21,0,3))
linkLIRRListenerAdded.setObjects(*((_C,_M),(_C,_I),(_C,_H),(_C,_D),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:linkLIRRListenerAdded.setStatus(_A)
linkLIRRListenerRemoved=NotificationType((1,3,6,1,4,1,1588,2,1,1,50,21,0,4))
linkLIRRListenerRemoved.setObjects(*((_C,_M),(_C,_I),(_C,_H),(_C,_D),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:linkLIRRListenerRemoved.setStatus(_A)
linkRLIRFailureIncident=NotificationType((1,3,6,1,4,1,1588,2,1,1,50,21,0,5))
linkRLIRFailureIncident.setObjects(*((_C,_G),(_C,_H),(_C,_Q),(_C,_R),(_C,_J),(_C,_S),(_C,_I),(_C,_D),(_C,_E),(_C,_F)))
if mibBuilder.loadTexts:linkRLIRFailureIncident.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FcPortID':FcPortID,'RLIRLinkFailureType':RLIRLinkFailureType,'LinkWwn':LinkWwn,'PortType':PortType,'LinkFormat':LinkFormat,'RegType':RegType,'LIRRProtocol':LIRRProtocol,'RNIDTagType':RNIDTagType,'RNIDFlags':RNIDFlags,'RNIDType':RNIDType,'RNIDModel':RNIDModel,'RNIDManufacturer':RNIDManufacturer,'RNIDManufacturerPlant':RNIDManufacturerPlant,'RNIDSequenceNumber':RNIDSequenceNumber,'RNIDParams':RNIDParams,'linkIncidentMIB':linkIncidentMIB,'ficonRNID':ficonRNID,'nodeRNIDTableNumEntries':nodeRNIDTableNumEntries,'nodeRNIDTable':nodeRNIDTable,'nodeRNIDEntry':nodeRNIDEntry,_G:nodeRNIDIndex,_K:nodeRNIDIncidentPortWWN,'nodeRNIDPID':nodeRNIDPID,'nodeRNIDFlags':nodeRNIDFlags,'nodeRNIDType':nodeRNIDType,'nodeRNIDModel':nodeRNIDModel,'nodeRNIDManufacturer':nodeRNIDManufacturer,'nodeRNIDManufacturerPlant':nodeRNIDManufacturerPlant,'nodeRNIDSequenceNumber':nodeRNIDSequenceNumber,_L:nodeRNIDConnectedPortWWN,'nodeRNIDPortType':nodeRNIDPortType,'nodeRNIDFormat':nodeRNIDFormat,'nodeRNIDTag':nodeRNIDTag,'nodeRNIDParams':nodeRNIDParams,'switchRNIDTableNumEntries':switchRNIDTableNumEntries,'switchRNIDTable':switchRNIDTable,'switchRNIDEntry':switchRNIDEntry,_P:switchRNIDIndex,'switchRNIDSwitchWWN':switchRNIDSwitchWWN,'switchRNIDFlags':switchRNIDFlags,'switchRNIDType':switchRNIDType,'switchRNIDModel':switchRNIDModel,'switchRNIDManufacturer':switchRNIDManufacturer,'switchRNIDManufacturerPlant':switchRNIDManufacturerPlant,'switchRNIDSequenceNumber':switchRNIDSequenceNumber,'switchRNIDTag':switchRNIDTag,'switchRNIDParams':switchRNIDParams,_D:nodeVfId,_E:ficonSlot,_F:ficonPort,'ficonLIRR':ficonLIRR,'lIRRTableNumEntries':lIRRTableNumEntries,'lIRRTable':lIRRTable,'lIRREntry':lIRREntry,_H:lIRRIndex,_M:lIRRListenerPortWWN,_I:lIRRListenerPID,'lIRRRegType':lIRRRegType,'lIRRProtocol':lIRRProtocol,'lIRRPortType':lIRRPortType,'lIRRFormat':lIRRFormat,'ficonRLIR':ficonRLIR,'rLIRTableNumEntries':rLIRTableNumEntries,'rLIRTable':rLIRTable,'rLIREntry':rLIREntry,_J:rLIRIndex,_Q:rLIRIncidentPortWwn,'rLIRIncidentNodeWwn':rLIRIncidentNodeWwn,'rLIRIncidentPortType':rLIRIncidentPortType,'rLIRIncidentPID':rLIRIncidentPID,'rLIRIncidentPortNumber':rLIRIncidentPortNumber,_R:rLIRConnectedPortWwn,'rLIRConnectedNodeWwn':rLIRConnectedNodeWwn,'rLIRFabricWwn':rLIRFabricWwn,_S:rLIRLinkFailureType,'rLIRTimeStamp':rLIRTimeStamp,'rLIRFormat':rLIRFormat,'linkIncidentMIBTraps':linkIncidentMIBTraps,'linkIncidentMIBTrapPrefix':linkIncidentMIBTrapPrefix,'linkRNIDDeviceRegistration':linkRNIDDeviceRegistration,'linkRNIDDeviceDeRegistration':linkRNIDDeviceDeRegistration,'linkLIRRListenerAdded':linkLIRRListenerAdded,'linkLIRRListenerRemoved':linkLIRRListenerRemoved,'linkRLIRFailureIncident':linkRLIRFailureIncident})