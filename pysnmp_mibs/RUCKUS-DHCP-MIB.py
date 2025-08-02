_E='ruckusDHCPClientHWAddress'
_D='RUCKUS-DHCP-MIB'
_C='TruthValue'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonDHCPModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonDHCPModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_C)
ruckusDHCPMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,7,1))
_RuckusDHCPObjects_ObjectIdentity=ObjectIdentity
ruckusDHCPObjects=_RuckusDHCPObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,7,1,1))
_RuckusDHCPClientInfo_ObjectIdentity=ObjectIdentity
ruckusDHCPClientInfo=_RuckusDHCPClientInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,7,1,1,1))
_RuckusDHCPClientTable_Object=MibTable
ruckusDHCPClientTable=_RuckusDHCPClientTable_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1))
if mibBuilder.loadTexts:ruckusDHCPClientTable.setStatus(_A)
_RuckusDHCPClientEntry_Object=MibTableRow
ruckusDHCPClientEntry=_RuckusDHCPClientEntry_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1,1))
ruckusDHCPClientEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ruckusDHCPClientEntry.setStatus(_A)
_RuckusDHCPClientHWAddress_Type=MacAddress
_RuckusDHCPClientHWAddress_Object=MibTableColumn
ruckusDHCPClientHWAddress=_RuckusDHCPClientHWAddress_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1,1,1),_RuckusDHCPClientHWAddress_Type())
ruckusDHCPClientHWAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ruckusDHCPClientHWAddress.setStatus(_A)
_RuckusDHCPClientIPAddress_Type=IpAddress
_RuckusDHCPClientIPAddress_Object=MibTableColumn
ruckusDHCPClientIPAddress=_RuckusDHCPClientIPAddress_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1,1,2),_RuckusDHCPClientIPAddress_Type())
ruckusDHCPClientIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDHCPClientIPAddress.setStatus(_A)
_RuckusDHCPClientSubnetMask_Type=IpAddress
_RuckusDHCPClientSubnetMask_Object=MibTableColumn
ruckusDHCPClientSubnetMask=_RuckusDHCPClientSubnetMask_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1,1,3),_RuckusDHCPClientSubnetMask_Type())
ruckusDHCPClientSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDHCPClientSubnetMask.setStatus(_A)
_RuckusDHCPClientLeaseTime_Type=Unsigned32
_RuckusDHCPClientLeaseTime_Object=MibTableColumn
ruckusDHCPClientLeaseTime=_RuckusDHCPClientLeaseTime_Object((1,3,6,1,4,1,25053,1,1,7,1,1,1,1,1,4),_RuckusDHCPClientLeaseTime_Type())
ruckusDHCPClientLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDHCPClientLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:ruckusDHCPClientLeaseTime.setUnits('seconds')
_RuckusDHCPClientExternal_ObjectIdentity=ObjectIdentity
ruckusDHCPClientExternal=_RuckusDHCPClientExternal_ObjectIdentity((1,3,6,1,4,1,25053,1,1,7,1,1,2))
class _RuckusDHCPClientExternalRenew_Type(TruthValue):defaultValue=1
_RuckusDHCPClientExternalRenew_Type.__name__=_C
_RuckusDHCPClientExternalRenew_Object=MibScalar
ruckusDHCPClientExternalRenew=_RuckusDHCPClientExternalRenew_Object((1,3,6,1,4,1,25053,1,1,7,1,1,2,1),_RuckusDHCPClientExternalRenew_Type())
ruckusDHCPClientExternalRenew.setMaxAccess('read-write')
if mibBuilder.loadTexts:ruckusDHCPClientExternalRenew.setStatus(_A)
_RuckusDHCPClientEvents_ObjectIdentity=ObjectIdentity
ruckusDHCPClientEvents=_RuckusDHCPClientEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,7,1,2))
mibBuilder.exportSymbols(_D,**{'ruckusDHCPMIB':ruckusDHCPMIB,'ruckusDHCPObjects':ruckusDHCPObjects,'ruckusDHCPClientInfo':ruckusDHCPClientInfo,'ruckusDHCPClientTable':ruckusDHCPClientTable,'ruckusDHCPClientEntry':ruckusDHCPClientEntry,_E:ruckusDHCPClientHWAddress,'ruckusDHCPClientIPAddress':ruckusDHCPClientIPAddress,'ruckusDHCPClientSubnetMask':ruckusDHCPClientSubnetMask,'ruckusDHCPClientLeaseTime':ruckusDHCPClientLeaseTime,'ruckusDHCPClientExternal':ruckusDHCPClientExternal,'ruckusDHCPClientExternalRenew':ruckusDHCPClientExternalRenew,'ruckusDHCPClientEvents':ruckusDHCPClientEvents})