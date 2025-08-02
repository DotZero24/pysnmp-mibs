_E='disabled'
_D='enabled'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsBeepServer=ModuleIdentity((1,3,6,1,4,1,10876,101,2,18))
if mibBuilder.loadTexts:fsBeepServer.setRevisions(('2012-09-05 00:00',))
_FsBeepServerScalars_ObjectIdentity=ObjectIdentity
fsBeepServerScalars=_FsBeepServerScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,18,1))
class _FsBeepServerAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsBeepServerAdminStatus_Type.__name__=_A
_FsBeepServerAdminStatus_Object=MibScalar
fsBeepServerAdminStatus=_FsBeepServerAdminStatus_Object((1,3,6,1,4,1,10876,101,2,18,1,1),_FsBeepServerAdminStatus_Type())
fsBeepServerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBeepServerAdminStatus.setStatus(_B)
class _FsBeepServerRawProfile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsBeepServerRawProfile_Type.__name__=_A
_FsBeepServerRawProfile_Object=MibScalar
fsBeepServerRawProfile=_FsBeepServerRawProfile_Object((1,3,6,1,4,1,10876,101,2,18,1,2),_FsBeepServerRawProfile_Type())
fsBeepServerRawProfile.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsBeepServerRawProfile.setStatus(_B)
class _FsBeepServerIpv4PortNum_Type(Integer32):defaultValue=601;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsBeepServerIpv4PortNum_Type.__name__=_A
_FsBeepServerIpv4PortNum_Object=MibScalar
fsBeepServerIpv4PortNum=_FsBeepServerIpv4PortNum_Object((1,3,6,1,4,1,10876,101,2,18,1,3),_FsBeepServerIpv4PortNum_Type())
fsBeepServerIpv4PortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBeepServerIpv4PortNum.setStatus(_B)
class _FsBeepServerIpv6PortNum_Type(Integer32):defaultValue=601;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsBeepServerIpv6PortNum_Type.__name__=_A
_FsBeepServerIpv6PortNum_Object=MibScalar
fsBeepServerIpv6PortNum=_FsBeepServerIpv6PortNum_Object((1,3,6,1,4,1,10876,101,2,18,1,4),_FsBeepServerIpv6PortNum_Type())
fsBeepServerIpv6PortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsBeepServerIpv6PortNum.setStatus(_B)
mibBuilder.exportSymbols('SUPERMICRO-BEEP-SERVER-MIB',**{'fsBeepServer':fsBeepServer,'fsBeepServerScalars':fsBeepServerScalars,'fsBeepServerAdminStatus':fsBeepServerAdminStatus,'fsBeepServerRawProfile':fsBeepServerRawProfile,'fsBeepServerIpv4PortNum':fsBeepServerIpv4PortNum,'fsBeepServerIpv6PortNum':fsBeepServerIpv6PortNum})