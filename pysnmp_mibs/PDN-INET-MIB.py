_I='pdnInetIpAddress'
_H='PDN-INET-MIB'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pdn_inet=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,26))
if mibBuilder.loadTexts:pdn_inet.setRevisions(('1902-02-21 00:00','1900-05-10 00:00','1900-04-27 00:00'))
_PdnInetMIBObjects_ObjectIdentity=ObjectIdentity
pdnInetMIBObjects=_PdnInetMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,26,1))
class _PdnInetTelnetServerPort_Type(Integer32):defaultValue=23;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnInetTelnetServerPort_Type.__name__=_B
_PdnInetTelnetServerPort_Object=MibScalar
pdnInetTelnetServerPort=_PdnInetTelnetServerPort_Object((1,3,6,1,4,1,1795,2,24,2,26,1,1),_PdnInetTelnetServerPort_Type())
pdnInetTelnetServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnInetTelnetServerPort.setStatus(_A)
class _PdnInetFtpServerControlPort_Type(Integer32):defaultValue=21;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnInetFtpServerControlPort_Type.__name__=_B
_PdnInetFtpServerControlPort_Object=MibScalar
pdnInetFtpServerControlPort=_PdnInetFtpServerControlPort_Object((1,3,6,1,4,1,1795,2,24,2,26,1,2),_PdnInetFtpServerControlPort_Type())
pdnInetFtpServerControlPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnInetFtpServerControlPort.setStatus(_A)
class _PdnInetFtpServerDataPort_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PdnInetFtpServerDataPort_Type.__name__=_B
_PdnInetFtpServerDataPort_Object=MibScalar
pdnInetFtpServerDataPort=_PdnInetFtpServerDataPort_Object((1,3,6,1,4,1,1795,2,24,2,26,1,3),_PdnInetFtpServerDataPort_Type())
pdnInetFtpServerDataPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnInetFtpServerDataPort.setStatus(_A)
_PdnInetIpAddressTableMaxIpSubnets_Type=Integer32
_PdnInetIpAddressTableMaxIpSubnets_Object=MibScalar
pdnInetIpAddressTableMaxIpSubnets=_PdnInetIpAddressTableMaxIpSubnets_Object((1,3,6,1,4,1,1795,2,24,2,26,1,4),_PdnInetIpAddressTableMaxIpSubnets_Type())
pdnInetIpAddressTableMaxIpSubnets.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnInetIpAddressTableMaxIpSubnets.setStatus(_A)
_PdnInetIpAddressTableCurrentIpSubnets_Type=Integer32
_PdnInetIpAddressTableCurrentIpSubnets_Object=MibScalar
pdnInetIpAddressTableCurrentIpSubnets=_PdnInetIpAddressTableCurrentIpSubnets_Object((1,3,6,1,4,1,1795,2,24,2,26,1,5),_PdnInetIpAddressTableCurrentIpSubnets_Type())
pdnInetIpAddressTableCurrentIpSubnets.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnInetIpAddressTableCurrentIpSubnets.setStatus(_A)
_PdnInetIpAddressTable_Object=MibTable
pdnInetIpAddressTable=_PdnInetIpAddressTable_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6))
if mibBuilder.loadTexts:pdnInetIpAddressTable.setStatus(_A)
_PdnInetIpAddressTableEntry_Object=MibTableRow
pdnInetIpAddressTableEntry=_PdnInetIpAddressTableEntry_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1))
pdnInetIpAddressTableEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:pdnInetIpAddressTableEntry.setStatus(_A)
_PdnInetIpAddress_Type=IpAddress
_PdnInetIpAddress_Object=MibTableColumn
pdnInetIpAddress=_PdnInetIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1,1),_PdnInetIpAddress_Type())
pdnInetIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pdnInetIpAddress.setStatus(_A)
_PdnInetIpSubnetMask_Type=IpAddress
_PdnInetIpSubnetMask_Object=MibTableColumn
pdnInetIpSubnetMask=_PdnInetIpSubnetMask_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1,2),_PdnInetIpSubnetMask_Type())
pdnInetIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnInetIpSubnetMask.setStatus(_A)
class _PdnInetIpAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('primary',1),('secondary',2),('primaryBootp',3),('secondaryBootp',4)))
_PdnInetIpAddressType_Type.__name__=_B
_PdnInetIpAddressType_Object=MibTableColumn
pdnInetIpAddressType=_PdnInetIpAddressType_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1,3),_PdnInetIpAddressType_Type())
pdnInetIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnInetIpAddressType.setStatus(_A)
_PdnInetIpRowStatus_Type=RowStatus
_PdnInetIpRowStatus_Object=MibTableColumn
pdnInetIpRowStatus=_PdnInetIpRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1,4),_PdnInetIpRowStatus_Type())
pdnInetIpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnInetIpRowStatus.setStatus(_A)
_PdnInetIpGateway_Type=IpAddress
_PdnInetIpGateway_Object=MibTableColumn
pdnInetIpGateway=_PdnInetIpGateway_Object((1,3,6,1,4,1,1795,2,24,2,26,1,6,1,5),_PdnInetIpGateway_Type())
pdnInetIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnInetIpGateway.setStatus(_A)
_PdnInetMIBTraps_ObjectIdentity=ObjectIdentity
pdnInetMIBTraps=_PdnInetMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,26,2))
mibBuilder.exportSymbols(_H,**{'pdn-inet':pdn_inet,'pdnInetMIBObjects':pdnInetMIBObjects,'pdnInetTelnetServerPort':pdnInetTelnetServerPort,'pdnInetFtpServerControlPort':pdnInetFtpServerControlPort,'pdnInetFtpServerDataPort':pdnInetFtpServerDataPort,'pdnInetIpAddressTableMaxIpSubnets':pdnInetIpAddressTableMaxIpSubnets,'pdnInetIpAddressTableCurrentIpSubnets':pdnInetIpAddressTableCurrentIpSubnets,'pdnInetIpAddressTable':pdnInetIpAddressTable,'pdnInetIpAddressTableEntry':pdnInetIpAddressTableEntry,_I:pdnInetIpAddress,'pdnInetIpSubnetMask':pdnInetIpSubnetMask,'pdnInetIpAddressType':pdnInetIpAddressType,'pdnInetIpRowStatus':pdnInetIpRowStatus,'pdnInetIpGateway':pdnInetIpGateway,'pdnInetMIBTraps':pdnInetMIBTraps})