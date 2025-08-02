_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataFactory,=mibBuilder.importSymbols('BRCM-CABLEDATA-FACTORY-MIB','cableDataFactory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
usbFactory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,8))
if mibBuilder.loadTexts:usbFactory.setRevisions(('2007-02-05 00:00','2004-11-12 00:00','2004-08-25 00:00'))
_UsbFactMacAddress_Type=MacAddress
_UsbFactMacAddress_Object=MibScalar
usbFactMacAddress=_UsbFactMacAddress_Object((1,3,6,1,4,1,4413,2,99,1,1,2,8,1),_UsbFactMacAddress_Type())
usbFactMacAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:usbFactMacAddress.setStatus(_B)
_UsbFactVendorId_Type=Unsigned32
_UsbFactVendorId_Object=MibScalar
usbFactVendorId=_UsbFactVendorId_Object((1,3,6,1,4,1,4413,2,99,1,1,2,8,2),_UsbFactVendorId_Type())
usbFactVendorId.setMaxAccess(_A)
if mibBuilder.loadTexts:usbFactVendorId.setStatus(_B)
_UsbFactDeviceId_Type=Unsigned32
_UsbFactDeviceId_Object=MibScalar
usbFactDeviceId=_UsbFactDeviceId_Object((1,3,6,1,4,1,4413,2,99,1,1,2,8,3),_UsbFactDeviceId_Type())
usbFactDeviceId.setMaxAccess(_A)
if mibBuilder.loadTexts:usbFactDeviceId.setStatus(_B)
_UsbFactRNDISDriverEnable_Type=TruthValue
_UsbFactRNDISDriverEnable_Object=MibScalar
usbFactRNDISDriverEnable=_UsbFactRNDISDriverEnable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,8,4),_UsbFactRNDISDriverEnable_Type())
usbFactRNDISDriverEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:usbFactRNDISDriverEnable.setStatus(_B)
mibBuilder.exportSymbols('BRCM-USB-FACTORY-MIB',**{'usbFactory':usbFactory,'usbFactMacAddress':usbFactMacAddress,'usbFactVendorId':usbFactVendorId,'usbFactDeviceId':usbFactDeviceId,'usbFactRNDISDriverEnable':usbFactRNDISDriverEnable})