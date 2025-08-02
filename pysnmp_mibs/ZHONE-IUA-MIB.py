_G='zhoneIuaServerAddressIndex'
_F='ZHONE-IUA-MIB'
_E='Integer32'
_D='applIndex'
_C='NETWORK-SERVICES-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
applIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneIua,=mibBuilder.importSymbols('Zhone','zhoneIua')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneIuaModule=ModuleIdentity((1,3,6,1,4,1,5504,4,15,1))
if mibBuilder.loadTexts:zhoneIuaModule.setRevisions(('2009-05-25 23:16',))
_ZhoneIuaServerCfg_ObjectIdentity=ObjectIdentity
zhoneIuaServerCfg=_ZhoneIuaServerCfg_ObjectIdentity((1,3,6,1,4,1,5504,4,15,1,1))
_ZhoneIuaServerTable_Object=MibTable
zhoneIuaServerTable=_ZhoneIuaServerTable_Object((1,3,6,1,4,1,5504,4,15,1,1,1))
if mibBuilder.loadTexts:zhoneIuaServerTable.setStatus(_A)
_ZhoneIuaServerEntry_Object=MibTableRow
zhoneIuaServerEntry=_ZhoneIuaServerEntry_Object((1,3,6,1,4,1,5504,4,15,1,1,1,1))
zhoneIuaServerEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:zhoneIuaServerEntry.setStatus(_A)
_ZhoneIuaServerAddressIndex_Type=Unsigned32
_ZhoneIuaServerAddressIndex_Object=MibTableColumn
zhoneIuaServerAddressIndex=_ZhoneIuaServerAddressIndex_Object((1,3,6,1,4,1,5504,4,15,1,1,1,1,1),_ZhoneIuaServerAddressIndex_Type())
zhoneIuaServerAddressIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhoneIuaServerAddressIndex.setStatus(_A)
_ZhoneIuaServerRowStatus_Type=ZhoneRowStatus
_ZhoneIuaServerRowStatus_Object=MibTableColumn
zhoneIuaServerRowStatus=_ZhoneIuaServerRowStatus_Object((1,3,6,1,4,1,5504,4,15,1,1,1,1,2),_ZhoneIuaServerRowStatus_Type())
zhoneIuaServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIuaServerRowStatus.setStatus(_A)
_ZhoneIuaServerAddress_Type=InetAddress
_ZhoneIuaServerAddress_Object=MibTableColumn
zhoneIuaServerAddress=_ZhoneIuaServerAddress_Object((1,3,6,1,4,1,5504,4,15,1,1,1,1,3),_ZhoneIuaServerAddress_Type())
zhoneIuaServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIuaServerAddress.setStatus(_A)
class _ZhoneIuaServerPortNumber_Type(Integer32):defaultValue=9900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZhoneIuaServerPortNumber_Type.__name__=_E
_ZhoneIuaServerPortNumber_Object=MibTableColumn
zhoneIuaServerPortNumber=_ZhoneIuaServerPortNumber_Object((1,3,6,1,4,1,5504,4,15,1,1,1,1,4),_ZhoneIuaServerPortNumber_Type())
zhoneIuaServerPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneIuaServerPortNumber.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zhoneIuaModule':zhoneIuaModule,'zhoneIuaServerCfg':zhoneIuaServerCfg,'zhoneIuaServerTable':zhoneIuaServerTable,'zhoneIuaServerEntry':zhoneIuaServerEntry,_G:zhoneIuaServerAddressIndex,'zhoneIuaServerRowStatus':zhoneIuaServerRowStatus,'zhoneIuaServerAddress':zhoneIuaServerAddress,'zhoneIuaServerPortNumber':zhoneIuaServerPortNumber})