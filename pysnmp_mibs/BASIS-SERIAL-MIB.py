_K='basisSerialConfGroup'
_J='serialPortbps'
_I='serialPortEnable'
_H='serialPortType'
_G='serialPortNumOfValidEntries'
_F='read-write'
_E='read-only'
_D='serialPortNum'
_C='Integer32'
_B='BASIS-SERIAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
basisLines,=mibBuilder.importSymbols('BASIS-MIB','basisLines')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
basisSerialMIB=ModuleIdentity((1,3,6,1,4,1,351,150,69))
if mibBuilder.loadTexts:basisSerialMIB.setRevisions(('2003-05-03 00:00',))
_SerialInterface_ObjectIdentity=ObjectIdentity
serialInterface=_SerialInterface_ObjectIdentity((1,3,6,1,4,1,351,110,4,1))
_SerialInterfaceTable_Object=MibTable
serialInterfaceTable=_SerialInterfaceTable_Object((1,3,6,1,4,1,351,110,4,1,1))
if mibBuilder.loadTexts:serialInterfaceTable.setStatus(_A)
_SerialInterfaceEntry_Object=MibTableRow
serialInterfaceEntry=_SerialInterfaceEntry_Object((1,3,6,1,4,1,351,110,4,1,1,1))
serialInterfaceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:serialInterfaceEntry.setStatus(_A)
class _SerialPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SerialPortNum_Type.__name__=_C
_SerialPortNum_Object=MibTableColumn
serialPortNum=_SerialPortNum_Object((1,3,6,1,4,1,351,110,4,1,1,1,1),_SerialPortNum_Type())
serialPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:serialPortNum.setStatus(_A)
class _SerialPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('debug',2)))
_SerialPortType_Type.__name__=_C
_SerialPortType_Object=MibTableColumn
serialPortType=_SerialPortType_Object((1,3,6,1,4,1,351,110,4,1,1,1,2),_SerialPortType_Type())
serialPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:serialPortType.setStatus(_A)
class _SerialPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SerialPortEnable_Type.__name__=_C
_SerialPortEnable_Object=MibTableColumn
serialPortEnable=_SerialPortEnable_Object((1,3,6,1,4,1,351,110,4,1,1,1,3),_SerialPortEnable_Type())
serialPortEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:serialPortEnable.setStatus(_A)
class _SerialPortbps_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bps9600',1),('bps2400',2),('bps19200',3)))
_SerialPortbps_Type.__name__=_C
_SerialPortbps_Object=MibTableColumn
serialPortbps=_SerialPortbps_Object((1,3,6,1,4,1,351,110,4,1,1,1,4),_SerialPortbps_Type())
serialPortbps.setMaxAccess(_F)
if mibBuilder.loadTexts:serialPortbps.setStatus(_A)
class _SerialPortNumOfValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SerialPortNumOfValidEntries_Type.__name__=_C
_SerialPortNumOfValidEntries_Object=MibScalar
serialPortNumOfValidEntries=_SerialPortNumOfValidEntries_Object((1,3,6,1,4,1,351,110,4,1,2),_SerialPortNumOfValidEntries_Type())
serialPortNumOfValidEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:serialPortNumOfValidEntries.setStatus(_A)
_BasisSerialMIBConformance_ObjectIdentity=ObjectIdentity
basisSerialMIBConformance=_BasisSerialMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,69,2))
_BasisSerialMIBGroups_ObjectIdentity=ObjectIdentity
basisSerialMIBGroups=_BasisSerialMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,69,2,1))
_BasisSerialMIBCompliances_ObjectIdentity=ObjectIdentity
basisSerialMIBCompliances=_BasisSerialMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,69,2,2))
basisSerialConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,69,2,1,1))
basisSerialConfGroup.setObjects(*((_B,_G),(_B,_D),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:basisSerialConfGroup.setStatus(_A)
basisSerialCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,69,2,2,1))
basisSerialCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:basisSerialCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'serialInterface':serialInterface,'serialInterfaceTable':serialInterfaceTable,'serialInterfaceEntry':serialInterfaceEntry,_D:serialPortNum,_H:serialPortType,_I:serialPortEnable,_J:serialPortbps,_G:serialPortNumOfValidEntries,'basisSerialMIB':basisSerialMIB,'basisSerialMIBConformance':basisSerialMIBConformance,'basisSerialMIBGroups':basisSerialMIBGroups,_K:basisSerialConfGroup,'basisSerialMIBCompliances':basisSerialMIBCompliances,'basisSerialCompliance':basisSerialCompliance})