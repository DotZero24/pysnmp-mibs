_E='tibDeviceAddress'
_D='SCTE-HMS-TIB-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
transponderInterfaceBusIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','transponderInterfaceBusIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_TibAttachedDevices_Type=Integer32
_TibAttachedDevices_Object=MibScalar
tibAttachedDevices=_TibAttachedDevices_Object((1,3,6,1,4,1,5591,1,7,1),_TibAttachedDevices_Type())
tibAttachedDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:tibAttachedDevices.setStatus(_A)
_TibCommStatus_Type=Integer32
_TibCommStatus_Object=MibScalar
tibCommStatus=_TibCommStatus_Object((1,3,6,1,4,1,5591,1,7,2),_TibCommStatus_Type())
tibCommStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tibCommStatus.setStatus(_A)
_TibDevicesAddressedTable_Object=MibTable
tibDevicesAddressedTable=_TibDevicesAddressedTable_Object((1,3,6,1,4,1,5591,1,7,3))
if mibBuilder.loadTexts:tibDevicesAddressedTable.setStatus(_A)
_TibDevicesAddressedEntry_Object=MibTableRow
tibDevicesAddressedEntry=_TibDevicesAddressedEntry_Object((1,3,6,1,4,1,5591,1,7,3,1))
tibDevicesAddressedEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tibDevicesAddressedEntry.setStatus(_A)
class _TibDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_TibDeviceAddress_Type.__name__=_C
_TibDeviceAddress_Object=MibTableColumn
tibDeviceAddress=_TibDeviceAddress_Object((1,3,6,1,4,1,5591,1,7,3,1,1),_TibDeviceAddress_Type())
tibDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tibDeviceAddress.setStatus(_A)
_TibDeviceIdentity_Type=ObjectIdentifier
_TibDeviceIdentity_Object=MibTableColumn
tibDeviceIdentity=_TibDeviceIdentity_Object((1,3,6,1,4,1,5591,1,7,3,1,2),_TibDeviceIdentity_Type())
tibDeviceIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:tibDeviceIdentity.setStatus(_A)
class _TibControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('remote',1),('local',2),('notCommunicating',3)))
_TibControlMode_Type.__name__=_C
_TibControlMode_Object=MibTableColumn
tibControlMode=_TibControlMode_Object((1,3,6,1,4,1,5591,1,7,3,1,3),_TibControlMode_Type())
tibControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tibControlMode.setStatus('optional')
mibBuilder.exportSymbols(_D,**{'tibAttachedDevices':tibAttachedDevices,'tibCommStatus':tibCommStatus,'tibDevicesAddressedTable':tibDevicesAddressedTable,'tibDevicesAddressedEntry':tibDevicesAddressedEntry,_E:tibDeviceAddress,'tibDeviceIdentity':tibDeviceIdentity,'tibControlMode':tibControlMode})