_P='etsysRip2ExtGlobalGroup'
_O='etsysRip2ExtRouteFlushInterval'
_N='etsysRip2ExtRouteExpiryInterval'
_M='etsysRip2ExtRouteCheckInterval'
_L='etsysRip2ExtTriggeredDelayMax'
_K='etsysRip2ExtTriggeredDelayMin'
_J='etsysRip2ExtRefreshInterval'
_I='etsysRip2ExtMaxEcmpHops'
_H='etsysRip2ExtOperStatus'
_G='etsysRip2ExtAdminStatus'
_F='Integer32'
_E='seconds'
_D='read-write'
_C='Unsigned32'
_B='ENTERASYS-RIPv2-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysRip2ExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,66))
if mibBuilder.loadTexts:etsysRip2ExtMIB.setRevisions(('2009-02-06 17:11',))
_EtsysRip2ExtObjects_ObjectIdentity=ObjectIdentity
etsysRip2ExtObjects=_EtsysRip2ExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,66,1))
_EtsysRip2ExtGlobals_ObjectIdentity=ObjectIdentity
etsysRip2ExtGlobals=_EtsysRip2ExtGlobals_ObjectIdentity((1,3,6,1,4,1,5624,1,2,66,1,1))
class _EtsysRip2ExtAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
_EtsysRip2ExtAdminStatus_Type.__name__=_F
_EtsysRip2ExtAdminStatus_Object=MibScalar
etsysRip2ExtAdminStatus=_EtsysRip2ExtAdminStatus_Object((1,3,6,1,4,1,5624,1,2,66,1,1,1),_EtsysRip2ExtAdminStatus_Type())
etsysRip2ExtAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtAdminStatus.setStatus(_A)
class _EtsysRip2ExtOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
_EtsysRip2ExtOperStatus_Type.__name__=_F
_EtsysRip2ExtOperStatus_Object=MibScalar
etsysRip2ExtOperStatus=_EtsysRip2ExtOperStatus_Object((1,3,6,1,4,1,5624,1,2,66,1,1,2),_EtsysRip2ExtOperStatus_Type())
etsysRip2ExtOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysRip2ExtOperStatus.setStatus(_A)
class _EtsysRip2ExtMaxEcmpHops_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysRip2ExtMaxEcmpHops_Type.__name__=_C
_EtsysRip2ExtMaxEcmpHops_Object=MibScalar
etsysRip2ExtMaxEcmpHops=_EtsysRip2ExtMaxEcmpHops_Object((1,3,6,1,4,1,5624,1,2,66,1,1,3),_EtsysRip2ExtMaxEcmpHops_Type())
etsysRip2ExtMaxEcmpHops.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtMaxEcmpHops.setStatus(_A)
class _EtsysRip2ExtRefreshInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysRip2ExtRefreshInterval_Type.__name__=_C
_EtsysRip2ExtRefreshInterval_Object=MibScalar
etsysRip2ExtRefreshInterval=_EtsysRip2ExtRefreshInterval_Object((1,3,6,1,4,1,5624,1,2,66,1,1,4),_EtsysRip2ExtRefreshInterval_Type())
etsysRip2ExtRefreshInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtRefreshInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysRip2ExtRefreshInterval.setUnits(_E)
class _EtsysRip2ExtTriggeredDelayMin_Type(Unsigned32):defaultValue=1
_EtsysRip2ExtTriggeredDelayMin_Type.__name__=_C
_EtsysRip2ExtTriggeredDelayMin_Object=MibScalar
etsysRip2ExtTriggeredDelayMin=_EtsysRip2ExtTriggeredDelayMin_Object((1,3,6,1,4,1,5624,1,2,66,1,1,5),_EtsysRip2ExtTriggeredDelayMin_Type())
etsysRip2ExtTriggeredDelayMin.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtTriggeredDelayMin.setStatus(_A)
if mibBuilder.loadTexts:etsysRip2ExtTriggeredDelayMin.setUnits(_E)
class _EtsysRip2ExtTriggeredDelayMax_Type(Unsigned32):defaultValue=5
_EtsysRip2ExtTriggeredDelayMax_Type.__name__=_C
_EtsysRip2ExtTriggeredDelayMax_Object=MibScalar
etsysRip2ExtTriggeredDelayMax=_EtsysRip2ExtTriggeredDelayMax_Object((1,3,6,1,4,1,5624,1,2,66,1,1,6),_EtsysRip2ExtTriggeredDelayMax_Type())
etsysRip2ExtTriggeredDelayMax.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtTriggeredDelayMax.setStatus(_A)
if mibBuilder.loadTexts:etsysRip2ExtTriggeredDelayMax.setUnits(_E)
class _EtsysRip2ExtRouteCheckInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_EtsysRip2ExtRouteCheckInterval_Type.__name__=_C
_EtsysRip2ExtRouteCheckInterval_Object=MibScalar
etsysRip2ExtRouteCheckInterval=_EtsysRip2ExtRouteCheckInterval_Object((1,3,6,1,4,1,5624,1,2,66,1,1,7),_EtsysRip2ExtRouteCheckInterval_Type())
etsysRip2ExtRouteCheckInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtRouteCheckInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysRip2ExtRouteCheckInterval.setUnits(_E)
class _EtsysRip2ExtRouteExpiryInterval_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EtsysRip2ExtRouteExpiryInterval_Type.__name__=_C
_EtsysRip2ExtRouteExpiryInterval_Object=MibScalar
etsysRip2ExtRouteExpiryInterval=_EtsysRip2ExtRouteExpiryInterval_Object((1,3,6,1,4,1,5624,1,2,66,1,1,8),_EtsysRip2ExtRouteExpiryInterval_Type())
etsysRip2ExtRouteExpiryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtRouteExpiryInterval.setStatus(_A)
class _EtsysRip2ExtRouteFlushInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EtsysRip2ExtRouteFlushInterval_Type.__name__=_C
_EtsysRip2ExtRouteFlushInterval_Object=MibScalar
etsysRip2ExtRouteFlushInterval=_EtsysRip2ExtRouteFlushInterval_Object((1,3,6,1,4,1,5624,1,2,66,1,1,9),_EtsysRip2ExtRouteFlushInterval_Type())
etsysRip2ExtRouteFlushInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysRip2ExtRouteFlushInterval.setStatus(_A)
_EtsysRip2ExtConformance_ObjectIdentity=ObjectIdentity
etsysRip2ExtConformance=_EtsysRip2ExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,66,2))
_EtsysRip2ExtGroups_ObjectIdentity=ObjectIdentity
etsysRip2ExtGroups=_EtsysRip2ExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,66,2,1))
_EtsysRip2ExtCompliances_ObjectIdentity=ObjectIdentity
etsysRip2ExtCompliances=_EtsysRip2ExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,66,2,2))
etsysRip2ExtGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,66,2,1,1))
etsysRip2ExtGlobalGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:etsysRip2ExtGlobalGroup.setStatus(_A)
etsysRip2ExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,66,2,2,1))
etsysRip2ExtCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:etsysRip2ExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysRip2ExtMIB':etsysRip2ExtMIB,'etsysRip2ExtObjects':etsysRip2ExtObjects,'etsysRip2ExtGlobals':etsysRip2ExtGlobals,_G:etsysRip2ExtAdminStatus,_H:etsysRip2ExtOperStatus,_I:etsysRip2ExtMaxEcmpHops,_J:etsysRip2ExtRefreshInterval,_K:etsysRip2ExtTriggeredDelayMin,_L:etsysRip2ExtTriggeredDelayMax,_M:etsysRip2ExtRouteCheckInterval,_N:etsysRip2ExtRouteExpiryInterval,_O:etsysRip2ExtRouteFlushInterval,'etsysRip2ExtConformance':etsysRip2ExtConformance,'etsysRip2ExtGroups':etsysRip2ExtGroups,_P:etsysRip2ExtGlobalGroup,'etsysRip2ExtCompliances':etsysRip2ExtCompliances,'etsysRip2ExtCompliance':etsysRip2ExtCompliance})