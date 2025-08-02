_G='read-only'
_F='tpStaticMrouteSourceMask'
_E='tpStaticMrouteSource'
_D='Integer32'
_C='read-create'
_B='TPLINK-STATICMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkStaticMrouteMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,79))
if mibBuilder.loadTexts:tplinkStaticMrouteMIB.setRevisions(('2012-12-13 09:30',))
_TplinkStaticMrouteMIBObjects_ObjectIdentity=ObjectIdentity
tplinkStaticMrouteMIBObjects=_TplinkStaticMrouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,79,1))
_TplinkStaticMrouteConfig_ObjectIdentity=ObjectIdentity
tplinkStaticMrouteConfig=_TplinkStaticMrouteConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,79,1,1))
_TpStaticMrouteTable_Object=MibTable
tpStaticMrouteTable=_TpStaticMrouteTable_Object((1,3,6,1,4,1,11863,6,79,1,1,1))
if mibBuilder.loadTexts:tpStaticMrouteTable.setStatus(_A)
_TpStaticMrouteEntry_Object=MibTableRow
tpStaticMrouteEntry=_TpStaticMrouteEntry_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1))
tpStaticMrouteEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:tpStaticMrouteEntry.setStatus(_A)
_TpStaticMrouteSource_Type=IpAddress
_TpStaticMrouteSource_Object=MibTableColumn
tpStaticMrouteSource=_TpStaticMrouteSource_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1,1),_TpStaticMrouteSource_Type())
tpStaticMrouteSource.setMaxAccess(_G)
if mibBuilder.loadTexts:tpStaticMrouteSource.setStatus(_A)
_TpStaticMrouteSourceMask_Type=IpAddress
_TpStaticMrouteSourceMask_Object=MibTableColumn
tpStaticMrouteSourceMask=_TpStaticMrouteSourceMask_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1,2),_TpStaticMrouteSourceMask_Type())
tpStaticMrouteSourceMask.setMaxAccess(_G)
if mibBuilder.loadTexts:tpStaticMrouteSourceMask.setStatus(_A)
_TpStaticMrouteRpfNeigbor_Type=IpAddress
_TpStaticMrouteRpfNeigbor_Object=MibTableColumn
tpStaticMrouteRpfNeigbor=_TpStaticMrouteRpfNeigbor_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1,3),_TpStaticMrouteRpfNeigbor_Type())
tpStaticMrouteRpfNeigbor.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticMrouteRpfNeigbor.setStatus(_A)
class _TpStaticMrouteDistance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TpStaticMrouteDistance_Type.__name__=_D
_TpStaticMrouteDistance_Object=MibTableColumn
tpStaticMrouteDistance=_TpStaticMrouteDistance_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1,4),_TpStaticMrouteDistance_Type())
tpStaticMrouteDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticMrouteDistance.setStatus(_A)
_TpStaticMrouteStatus_Type=TPRowStatus
_TpStaticMrouteStatus_Object=MibTableColumn
tpStaticMrouteStatus=_TpStaticMrouteStatus_Object((1,3,6,1,4,1,11863,6,79,1,1,1,1,5),_TpStaticMrouteStatus_Type())
tpStaticMrouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStaticMrouteStatus.setStatus(_A)
_TplinkStaticMrouteNotifications_ObjectIdentity=ObjectIdentity
tplinkStaticMrouteNotifications=_TplinkStaticMrouteNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,79,2))
mibBuilder.exportSymbols(_B,**{'tplinkStaticMrouteMIB':tplinkStaticMrouteMIB,'tplinkStaticMrouteMIBObjects':tplinkStaticMrouteMIBObjects,'tplinkStaticMrouteConfig':tplinkStaticMrouteConfig,'tpStaticMrouteTable':tpStaticMrouteTable,'tpStaticMrouteEntry':tpStaticMrouteEntry,_E:tpStaticMrouteSource,_F:tpStaticMrouteSourceMask,'tpStaticMrouteRpfNeigbor':tpStaticMrouteRpfNeigbor,'tpStaticMrouteDistance':tpStaticMrouteDistance,'tpStaticMrouteStatus':tpStaticMrouteStatus,'tplinkStaticMrouteNotifications':tplinkStaticMrouteNotifications})