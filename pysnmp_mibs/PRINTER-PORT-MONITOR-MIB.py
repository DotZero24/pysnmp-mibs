_f='ppmPortGroup'
_e='ppmPrinterGroup'
_d='ppmGeneralGroup'
_c='ppmPortLprByteCountEnabled'
_b='ppmPortPrtChannelIndex'
_a='ppmPortProtocolAltSourceEnabled'
_Z='ppmPortProtocolTargetPort'
_Y='ppmPortProtocolType'
_X='ppmPortServiceNameOrURI'
_W='ppmPortName'
_V='ppmPortEnabled'
_U='ppmPrinterSnmpQueryEnabled'
_T='ppmPrinterSnmpCommunityName'
_S='ppmPrinterHrDeviceIndex'
_R='ppmPrinterPreferredPortIndex'
_Q='ppmPrinterNumberOfPorts'
_P='ppmPrinterIEEE1284DeviceId'
_O='ppmPrinterName'
_N='ppmGeneralNumberOfPorts'
_M='ppmGeneralNumberOfPrinters'
_L='ppmGeneralNaturalLanguage'
_K='ppmPortIndex'
_J='not-accessible'
_I='ppmPrinterIndex'
_H='OctetString'
_G='Gauge32'
_F='TruthValue'
_E='SnmpAdminString'
_D='Integer32'
_C='read-only'
_B='PRINTER-PORT-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_G,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ppmMIB=ModuleIdentity((1,3,6,1,4,1,2699,1,2))
if mibBuilder.loadTexts:ppmMIB.setRevisions(('2005-10-25 00:00',))
_PpmMIBObjects_ObjectIdentity=ObjectIdentity
ppmMIBObjects=_PpmMIBObjects_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1))
_PpmGeneral_ObjectIdentity=ObjectIdentity
ppmGeneral=_PpmGeneral_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,1))
class _PpmGeneralNaturalLanguage_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PpmGeneralNaturalLanguage_Type.__name__=_E
_PpmGeneralNaturalLanguage_Object=MibScalar
ppmGeneralNaturalLanguage=_PpmGeneralNaturalLanguage_Object((1,3,6,1,4,1,2699,1,2,1,1,1),_PpmGeneralNaturalLanguage_Type())
ppmGeneralNaturalLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmGeneralNaturalLanguage.setStatus(_A)
class _PpmGeneralNumberOfPrinters_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPrinters_Type.__name__=_G
_PpmGeneralNumberOfPrinters_Object=MibScalar
ppmGeneralNumberOfPrinters=_PpmGeneralNumberOfPrinters_Object((1,3,6,1,4,1,2699,1,2,1,1,2),_PpmGeneralNumberOfPrinters_Type())
ppmGeneralNumberOfPrinters.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmGeneralNumberOfPrinters.setStatus(_A)
class _PpmGeneralNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmGeneralNumberOfPorts_Type.__name__=_G
_PpmGeneralNumberOfPorts_Object=MibScalar
ppmGeneralNumberOfPorts=_PpmGeneralNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,1,3),_PpmGeneralNumberOfPorts_Type())
ppmGeneralNumberOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmGeneralNumberOfPorts.setStatus(_A)
_PpmPrinter_ObjectIdentity=ObjectIdentity
ppmPrinter=_PpmPrinter_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,2))
_PpmPrinterTable_Object=MibTable
ppmPrinterTable=_PpmPrinterTable_Object((1,3,6,1,4,1,2699,1,2,1,2,1))
if mibBuilder.loadTexts:ppmPrinterTable.setStatus(_A)
_PpmPrinterEntry_Object=MibTableRow
ppmPrinterEntry=_PpmPrinterEntry_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1))
ppmPrinterEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ppmPrinterEntry.setStatus(_A)
class _PpmPrinterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PpmPrinterIndex_Type.__name__=_D
_PpmPrinterIndex_Object=MibTableColumn
ppmPrinterIndex=_PpmPrinterIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,1),_PpmPrinterIndex_Type())
ppmPrinterIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ppmPrinterIndex.setStatus(_A)
class _PpmPrinterName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPrinterName_Type.__name__=_E
_PpmPrinterName_Object=MibTableColumn
ppmPrinterName=_PpmPrinterName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,2),_PpmPrinterName_Type())
ppmPrinterName.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterName.setStatus(_A)
class _PpmPrinterIEEE1284DeviceId_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
_PpmPrinterIEEE1284DeviceId_Type.__name__=_H
_PpmPrinterIEEE1284DeviceId_Object=MibTableColumn
ppmPrinterIEEE1284DeviceId=_PpmPrinterIEEE1284DeviceId_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,3),_PpmPrinterIEEE1284DeviceId_Type())
ppmPrinterIEEE1284DeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterIEEE1284DeviceId.setStatus(_A)
class _PpmPrinterNumberOfPorts_Type(Gauge32):defaultValue=0
_PpmPrinterNumberOfPorts_Type.__name__=_G
_PpmPrinterNumberOfPorts_Object=MibTableColumn
ppmPrinterNumberOfPorts=_PpmPrinterNumberOfPorts_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,4),_PpmPrinterNumberOfPorts_Type())
ppmPrinterNumberOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterNumberOfPorts.setStatus(_A)
class _PpmPrinterPreferredPortIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterPreferredPortIndex_Type.__name__=_D
_PpmPrinterPreferredPortIndex_Object=MibTableColumn
ppmPrinterPreferredPortIndex=_PpmPrinterPreferredPortIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,5),_PpmPrinterPreferredPortIndex_Type())
ppmPrinterPreferredPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterPreferredPortIndex.setStatus(_A)
class _PpmPrinterHrDeviceIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPrinterHrDeviceIndex_Type.__name__=_D
_PpmPrinterHrDeviceIndex_Object=MibTableColumn
ppmPrinterHrDeviceIndex=_PpmPrinterHrDeviceIndex_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,6),_PpmPrinterHrDeviceIndex_Type())
ppmPrinterHrDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterHrDeviceIndex.setStatus(_A)
class _PpmPrinterSnmpCommunityName_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPrinterSnmpCommunityName_Type.__name__=_H
_PpmPrinterSnmpCommunityName_Object=MibTableColumn
ppmPrinterSnmpCommunityName=_PpmPrinterSnmpCommunityName_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,7),_PpmPrinterSnmpCommunityName_Type())
ppmPrinterSnmpCommunityName.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterSnmpCommunityName.setStatus(_A)
class _PpmPrinterSnmpQueryEnabled_Type(TruthValue):defaultValue=2
_PpmPrinterSnmpQueryEnabled_Type.__name__=_F
_PpmPrinterSnmpQueryEnabled_Object=MibTableColumn
ppmPrinterSnmpQueryEnabled=_PpmPrinterSnmpQueryEnabled_Object((1,3,6,1,4,1,2699,1,2,1,2,1,1,8),_PpmPrinterSnmpQueryEnabled_Type())
ppmPrinterSnmpQueryEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPrinterSnmpQueryEnabled.setStatus(_A)
_PpmPort_ObjectIdentity=ObjectIdentity
ppmPort=_PpmPort_ObjectIdentity((1,3,6,1,4,1,2699,1,2,1,3))
_PpmPortTable_Object=MibTable
ppmPortTable=_PpmPortTable_Object((1,3,6,1,4,1,2699,1,2,1,3,1))
if mibBuilder.loadTexts:ppmPortTable.setStatus(_A)
_PpmPortEntry_Object=MibTableRow
ppmPortEntry=_PpmPortEntry_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1))
ppmPortEntry.setIndexNames((0,_B,_I),(0,_B,_K))
if mibBuilder.loadTexts:ppmPortEntry.setStatus(_A)
class _PpmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PpmPortIndex_Type.__name__=_D
_PpmPortIndex_Object=MibTableColumn
ppmPortIndex=_PpmPortIndex_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,1),_PpmPortIndex_Type())
ppmPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ppmPortIndex.setStatus(_A)
class _PpmPortEnabled_Type(TruthValue):defaultValue=2
_PpmPortEnabled_Type.__name__=_F
_PpmPortEnabled_Object=MibTableColumn
ppmPortEnabled=_PpmPortEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,2),_PpmPortEnabled_Type())
ppmPortEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortEnabled.setStatus(_A)
class _PpmPortName_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_PpmPortName_Type.__name__=_E
_PpmPortName_Object=MibTableColumn
ppmPortName=_PpmPortName_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,3),_PpmPortName_Type())
ppmPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortName.setStatus(_A)
class _PpmPortServiceNameOrURI_Type(SnmpAdminString):defaultHexValue='';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PpmPortServiceNameOrURI_Type.__name__=_E
_PpmPortServiceNameOrURI_Object=MibTableColumn
ppmPortServiceNameOrURI=_PpmPortServiceNameOrURI_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,4),_PpmPortServiceNameOrURI_Type())
ppmPortServiceNameOrURI.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortServiceNameOrURI.setStatus(_A)
class _PpmPortProtocolType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PpmPortProtocolType_Type.__name__=_D
_PpmPortProtocolType_Object=MibTableColumn
ppmPortProtocolType=_PpmPortProtocolType_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,5),_PpmPortProtocolType_Type())
ppmPortProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortProtocolType.setStatus(_A)
class _PpmPortProtocolTargetPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortProtocolTargetPort_Type.__name__=_D
_PpmPortProtocolTargetPort_Object=MibTableColumn
ppmPortProtocolTargetPort=_PpmPortProtocolTargetPort_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,6),_PpmPortProtocolTargetPort_Type())
ppmPortProtocolTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortProtocolTargetPort.setStatus(_A)
class _PpmPortProtocolAltSourceEnabled_Type(TruthValue):defaultValue=2
_PpmPortProtocolAltSourceEnabled_Type.__name__=_F
_PpmPortProtocolAltSourceEnabled_Object=MibTableColumn
ppmPortProtocolAltSourceEnabled=_PpmPortProtocolAltSourceEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,7),_PpmPortProtocolAltSourceEnabled_Type())
ppmPortProtocolAltSourceEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortProtocolAltSourceEnabled.setStatus(_A)
class _PpmPortPrtChannelIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PpmPortPrtChannelIndex_Type.__name__=_D
_PpmPortPrtChannelIndex_Object=MibTableColumn
ppmPortPrtChannelIndex=_PpmPortPrtChannelIndex_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,8),_PpmPortPrtChannelIndex_Type())
ppmPortPrtChannelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortPrtChannelIndex.setStatus(_A)
class _PpmPortLprByteCountEnabled_Type(TruthValue):defaultValue=2
_PpmPortLprByteCountEnabled_Type.__name__=_F
_PpmPortLprByteCountEnabled_Object=MibTableColumn
ppmPortLprByteCountEnabled=_PpmPortLprByteCountEnabled_Object((1,3,6,1,4,1,2699,1,2,1,3,1,1,9),_PpmPortLprByteCountEnabled_Type())
ppmPortLprByteCountEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ppmPortLprByteCountEnabled.setStatus(_A)
_PpmMIBConformance_ObjectIdentity=ObjectIdentity
ppmMIBConformance=_PpmMIBConformance_ObjectIdentity((1,3,6,1,4,1,2699,1,2,2))
_PpmMIBObjectGroups_ObjectIdentity=ObjectIdentity
ppmMIBObjectGroups=_PpmMIBObjectGroups_ObjectIdentity((1,3,6,1,4,1,2699,1,2,2,2))
ppmGeneralGroup=ObjectGroup((1,3,6,1,4,1,2699,1,2,2,2,1))
ppmGeneralGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ppmGeneralGroup.setStatus(_A)
ppmPrinterGroup=ObjectGroup((1,3,6,1,4,1,2699,1,2,2,2,2))
ppmPrinterGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ppmPrinterGroup.setStatus(_A)
ppmPortGroup=ObjectGroup((1,3,6,1,4,1,2699,1,2,2,2,3))
ppmPortGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ppmPortGroup.setStatus(_A)
ppmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2699,1,2,2,1))
ppmMIBCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ppmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ppmMIB':ppmMIB,'ppmMIBObjects':ppmMIBObjects,'ppmGeneral':ppmGeneral,_L:ppmGeneralNaturalLanguage,_M:ppmGeneralNumberOfPrinters,_N:ppmGeneralNumberOfPorts,'ppmPrinter':ppmPrinter,'ppmPrinterTable':ppmPrinterTable,'ppmPrinterEntry':ppmPrinterEntry,_I:ppmPrinterIndex,_O:ppmPrinterName,_P:ppmPrinterIEEE1284DeviceId,_Q:ppmPrinterNumberOfPorts,_R:ppmPrinterPreferredPortIndex,_S:ppmPrinterHrDeviceIndex,_T:ppmPrinterSnmpCommunityName,_U:ppmPrinterSnmpQueryEnabled,'ppmPort':ppmPort,'ppmPortTable':ppmPortTable,'ppmPortEntry':ppmPortEntry,_K:ppmPortIndex,_V:ppmPortEnabled,_W:ppmPortName,_X:ppmPortServiceNameOrURI,_Y:ppmPortProtocolType,_Z:ppmPortProtocolTargetPort,_a:ppmPortProtocolAltSourceEnabled,_b:ppmPortPrtChannelIndex,_c:ppmPortLprByteCountEnabled,'ppmMIBConformance':ppmMIBConformance,'ppmMIBCompliance':ppmMIBCompliance,'ppmMIBObjectGroups':ppmMIBObjectGroups,_d:ppmGeneralGroup,_e:ppmPrinterGroup,_f:ppmPortGroup})