_F='imimAddressChassisSlot'
_E='CTRON-IMIM-ADDRESS-MIB'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_CommsDevice_ObjectIdentity=ObjectIdentity
commsDevice=_CommsDevice_ObjectIdentity((1,3,6,1,4,1,52,1))
_Subsystem_ObjectIdentity=ObjectIdentity
subsystem=_Subsystem_ObjectIdentity((1,3,6,1,4,1,52,1,6))
_BackplaneProtocol_ObjectIdentity=ObjectIdentity
backplaneProtocol=_BackplaneProtocol_ObjectIdentity((1,3,6,1,4,1,52,1,6,5))
_ImimAddress_ObjectIdentity=ObjectIdentity
imimAddress=_ImimAddress_ObjectIdentity((1,3,6,1,4,1,52,1,6,5,1))
_ImimAddressTable_Object=MibTable
imimAddressTable=_ImimAddressTable_Object((1,3,6,1,4,1,52,1,6,5,1,1))
if mibBuilder.loadTexts:imimAddressTable.setStatus(_A)
_ImimAddressEntry_Object=MibTableRow
imimAddressEntry=_ImimAddressEntry_Object((1,3,6,1,4,1,52,1,6,5,1,1,1))
imimAddressEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:imimAddressEntry.setStatus(_A)
class _ImimAddressChassisSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ImimAddressChassisSlot_Type.__name__=_D
_ImimAddressChassisSlot_Object=MibTableColumn
imimAddressChassisSlot=_ImimAddressChassisSlot_Object((1,3,6,1,4,1,52,1,6,5,1,1,1,1),_ImimAddressChassisSlot_Type())
imimAddressChassisSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:imimAddressChassisSlot.setStatus(_A)
class _ImimAddressMAC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_ImimAddressMAC_Type.__name__=_C
_ImimAddressMAC_Object=MibTableColumn
imimAddressMAC=_ImimAddressMAC_Object((1,3,6,1,4,1,52,1,6,5,1,1,1,2),_ImimAddressMAC_Type())
imimAddressMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:imimAddressMAC.setStatus(_A)
class _ImimAddressIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ImimAddressIP_Type.__name__=_C
_ImimAddressIP_Object=MibTableColumn
imimAddressIP=_ImimAddressIP_Object((1,3,6,1,4,1,52,1,6,5,1,1,1,3),_ImimAddressIP_Type())
imimAddressIP.setMaxAccess(_B)
if mibBuilder.loadTexts:imimAddressIP.setStatus(_A)
class _BackplaneHeartbeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('heartBeatPresent',1),('heartBeatAbsent',2),('notSupported',3)))
_BackplaneHeartbeat_Type.__name__=_D
_BackplaneHeartbeat_Object=MibScalar
backplaneHeartbeat=_BackplaneHeartbeat_Object((1,3,6,1,4,1,52,1,6,5,1,2),_BackplaneHeartbeat_Type())
backplaneHeartbeat.setMaxAccess(_B)
if mibBuilder.loadTexts:backplaneHeartbeat.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cabletron':cabletron,'commsDevice':commsDevice,'subsystem':subsystem,'backplaneProtocol':backplaneProtocol,'imimAddress':imimAddress,'imimAddressTable':imimAddressTable,'imimAddressEntry':imimAddressEntry,_F:imimAddressChassisSlot,'imimAddressMAC':imimAddressMAC,'imimAddressIP':imimAddressIP,'backplaneHeartbeat':backplaneHeartbeat})