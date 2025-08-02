_G='zxAnDlIntIndex'
_F='ZTE-AN-DHCP-L3PUB-MIB'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnDhcpL3PubMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,52))
_ZxAnDhcpL3PubMIBNotifs_ObjectIdentity=ObjectIdentity
zxAnDhcpL3PubMIBNotifs=_ZxAnDhcpL3PubMIBNotifs_ObjectIdentity((1,3,6,1,4,1,3902,1015,52,0))
_ZxAnDhcpL3PubMIBObjects_ObjectIdentity=ObjectIdentity
zxAnDhcpL3PubMIBObjects=_ZxAnDhcpL3PubMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,52,1))
_ZxAnDlGlobal_ObjectIdentity=ObjectIdentity
zxAnDlGlobal=_ZxAnDlGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1015,52,1,1))
class _ZxAnDlGlobalEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDlGlobalEnable_Type.__name__=_B
_ZxAnDlGlobalEnable_Object=MibScalar
zxAnDlGlobalEnable=_ZxAnDlGlobalEnable_Object((1,3,6,1,4,1,3902,1015,52,1,1,1),_ZxAnDlGlobalEnable_Type())
zxAnDlGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDlGlobalEnable.setStatus(_A)
class _ZxAnDlLog_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnDlLog_Type.__name__=_B
_ZxAnDlLog_Object=MibScalar
zxAnDlLog=_ZxAnDlLog_Object((1,3,6,1,4,1,3902,1015,52,1,1,2),_ZxAnDlLog_Type())
zxAnDlLog.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDlLog.setStatus(_A)
_ZxAnDlVlanInterface_ObjectIdentity=ObjectIdentity
zxAnDlVlanInterface=_ZxAnDlVlanInterface_ObjectIdentity((1,3,6,1,4,1,3902,1015,52,1,2))
_ZxAnDlVlanIntTable_Object=MibTable
zxAnDlVlanIntTable=_ZxAnDlVlanIntTable_Object((1,3,6,1,4,1,3902,1015,52,1,2,1))
if mibBuilder.loadTexts:zxAnDlVlanIntTable.setStatus(_A)
_ZxAnDlVlanIntEntry_Object=MibTableRow
zxAnDlVlanIntEntry=_ZxAnDlVlanIntEntry_Object((1,3,6,1,4,1,3902,1015,52,1,2,1,1))
zxAnDlVlanIntEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAnDlVlanIntEntry.setStatus(_A)
_ZxAnDlIntIndex_Type=ZxAnIfindex
_ZxAnDlIntIndex_Object=MibTableColumn
zxAnDlIntIndex=_ZxAnDlIntIndex_Object((1,3,6,1,4,1,3902,1015,52,1,2,1,1,1),_ZxAnDlIntIndex_Type())
zxAnDlIntIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnDlIntIndex.setStatus(_A)
class _ZxAnDlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('nowork',0),('server',1),('relay',2),('proxy',3)))
_ZxAnDlMode_Type.__name__=_B
_ZxAnDlMode_Object=MibTableColumn
zxAnDlMode=_ZxAnDlMode_Object((1,3,6,1,4,1,3902,1015,52,1,2,1,1,2),_ZxAnDlMode_Type())
zxAnDlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDlMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zxAnDhcpL3PubMIB':zxAnDhcpL3PubMIB,'zxAnDhcpL3PubMIBNotifs':zxAnDhcpL3PubMIBNotifs,'zxAnDhcpL3PubMIBObjects':zxAnDhcpL3PubMIBObjects,'zxAnDlGlobal':zxAnDlGlobal,'zxAnDlGlobalEnable':zxAnDlGlobalEnable,'zxAnDlLog':zxAnDlLog,'zxAnDlVlanInterface':zxAnDlVlanInterface,'zxAnDlVlanIntTable':zxAnDlVlanIntTable,'zxAnDlVlanIntEntry':zxAnDlVlanIntEntry,_G:zxAnDlIntIndex,'zxAnDlMode':zxAnDlMode})