_F='enabled'
_E='disabled'
_D='InterfaceIndexOrZero'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ruckusDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,46))
if mibBuilder.loadTexts:ruckusDhcpClientMIB.setRevisions(('2020-07-29 00:00',))
_RuckusDhcpClientGlobalObjects_ObjectIdentity=ObjectIdentity
ruckusDhcpClientGlobalObjects=_RuckusDhcpClientGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,46,1))
class _RuckusDhcpClientGlobalConfigState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RuckusDhcpClientGlobalConfigState_Type.__name__=_A
_RuckusDhcpClientGlobalConfigState_Object=MibScalar
ruckusDhcpClientGlobalConfigState=_RuckusDhcpClientGlobalConfigState_Object((1,3,6,1,4,1,1991,1,1,3,46,1,1),_RuckusDhcpClientGlobalConfigState_Type())
ruckusDhcpClientGlobalConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDhcpClientGlobalConfigState.setStatus(_C)
class _RuckusDhcpClientGlobalAutoUpdateConfigState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RuckusDhcpClientGlobalAutoUpdateConfigState_Type.__name__=_A
_RuckusDhcpClientGlobalAutoUpdateConfigState_Object=MibScalar
ruckusDhcpClientGlobalAutoUpdateConfigState=_RuckusDhcpClientGlobalAutoUpdateConfigState_Object((1,3,6,1,4,1,1991,1,1,3,46,1,2),_RuckusDhcpClientGlobalAutoUpdateConfigState_Type())
ruckusDhcpClientGlobalAutoUpdateConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDhcpClientGlobalAutoUpdateConfigState.setStatus(_C)
class _RuckusDhcpClientSpecificVEPort_Type(InterfaceIndexOrZero):defaultValue=0
_RuckusDhcpClientSpecificVEPort_Type.__name__=_D
_RuckusDhcpClientSpecificVEPort_Object=MibScalar
ruckusDhcpClientSpecificVEPort=_RuckusDhcpClientSpecificVEPort_Object((1,3,6,1,4,1,1991,1,1,3,46,1,3),_RuckusDhcpClientSpecificVEPort_Type())
ruckusDhcpClientSpecificVEPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDhcpClientSpecificVEPort.setStatus(_C)
mibBuilder.exportSymbols('RUCKUS-DHCPCLIENT-MIB',**{'ruckusDhcpClientMIB':ruckusDhcpClientMIB,'ruckusDhcpClientGlobalObjects':ruckusDhcpClientGlobalObjects,'ruckusDhcpClientGlobalConfigState':ruckusDhcpClientGlobalConfigState,'ruckusDhcpClientGlobalAutoUpdateConfigState':ruckusDhcpClientGlobalAutoUpdateConfigState,'ruckusDhcpClientSpecificVEPort':ruckusDhcpClientSpecificVEPort})