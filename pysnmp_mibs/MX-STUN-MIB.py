_V='stunServerGroupVer1'
_U='stunBasicGroupVer1'
_T='stunStaticPort'
_S='stunStaticHost'
_R='stunPort'
_Q='stunHost'
_P='stunNatBindingQueryInterval'
_O='stunKeepAliveInterval'
_N='stunQueryTimeout'
_M='stunQueryCacheDuration'
_L='stunEnable'
_K='stunStaticIndex'
_J='192.168.0.10'
_I='stunIndex'
_H='MxEnableState'
_G='MxIpPort'
_F='MxIpHostName'
_E='read-only'
_D='read-write'
_C='Unsigned32'
_B='MX-STUN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig')
MxEnableState,MxIpHostName,MxIpPort=mibBuilder.importSymbols('MX-TC',_H,_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stunMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,200))
if mibBuilder.loadTexts:stunMIB.setRevisions(('2004-12-10 00:00','2004-11-16 00:00','2004-11-09 00:00'))
_IpAddressStatusStun_ObjectIdentity=ObjectIdentity
ipAddressStatusStun=_IpAddressStatusStun_ObjectIdentity((1,3,6,1,4,1,4935,10,1,200))
_StunTable_Object=MibTable
stunTable=_StunTable_Object((1,3,6,1,4,1,4935,10,1,200,50))
if mibBuilder.loadTexts:stunTable.setStatus(_A)
_StunEntry_Object=MibTableRow
stunEntry=_StunEntry_Object((1,3,6,1,4,1,4935,10,1,200,50,50))
stunEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:stunEntry.setStatus(_A)
class _StunIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_StunIndex_Type.__name__=_C
_StunIndex_Object=MibTableColumn
stunIndex=_StunIndex_Object((1,3,6,1,4,1,4935,10,1,200,50,50,10),_StunIndex_Type())
stunIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:stunIndex.setStatus(_A)
class _StunHost_Type(MxIpHostName):defaultValue=OctetString(_J)
_StunHost_Type.__name__=_F
_StunHost_Object=MibTableColumn
stunHost=_StunHost_Object((1,3,6,1,4,1,4935,10,1,200,50,50,50),_StunHost_Type())
stunHost.setMaxAccess(_E)
if mibBuilder.loadTexts:stunHost.setStatus(_A)
class _StunPort_Type(MxIpPort):defaultValue=3478
_StunPort_Type.__name__=_G
_StunPort_Object=MibTableColumn
stunPort=_StunPort_Object((1,3,6,1,4,1,4935,10,1,200,50,50,100),_StunPort_Type())
stunPort.setMaxAccess(_E)
if mibBuilder.loadTexts:stunPort.setStatus(_A)
_IpAddressConfigStun_ObjectIdentity=ObjectIdentity
ipAddressConfigStun=_IpAddressConfigStun_ObjectIdentity((1,3,6,1,4,1,4935,15,1,200))
_IpAddressConfigStunStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigStunStatic=_IpAddressConfigStunStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,200,50))
_StunStaticTable_Object=MibTable
stunStaticTable=_StunStaticTable_Object((1,3,6,1,4,1,4935,15,1,200,50,50))
if mibBuilder.loadTexts:stunStaticTable.setStatus(_A)
_StunStaticEntry_Object=MibTableRow
stunStaticEntry=_StunStaticEntry_Object((1,3,6,1,4,1,4935,15,1,200,50,50,50))
stunStaticEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:stunStaticEntry.setStatus(_A)
class _StunStaticIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_StunStaticIndex_Type.__name__=_C
_StunStaticIndex_Object=MibTableColumn
stunStaticIndex=_StunStaticIndex_Object((1,3,6,1,4,1,4935,15,1,200,50,50,50,10),_StunStaticIndex_Type())
stunStaticIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:stunStaticIndex.setStatus(_A)
class _StunStaticHost_Type(MxIpHostName):defaultValue=OctetString(_J)
_StunStaticHost_Type.__name__=_F
_StunStaticHost_Object=MibTableColumn
stunStaticHost=_StunStaticHost_Object((1,3,6,1,4,1,4935,15,1,200,50,50,50,50),_StunStaticHost_Type())
stunStaticHost.setMaxAccess(_D)
if mibBuilder.loadTexts:stunStaticHost.setStatus(_A)
class _StunStaticPort_Type(MxIpPort):defaultValue=3478
_StunStaticPort_Type.__name__=_G
_StunStaticPort_Object=MibTableColumn
stunStaticPort=_StunStaticPort_Object((1,3,6,1,4,1,4935,15,1,200,50,50,50,100),_StunStaticPort_Type())
stunStaticPort.setMaxAccess(_D)
if mibBuilder.loadTexts:stunStaticPort.setStatus(_A)
_StunMIBObjects_ObjectIdentity=ObjectIdentity
stunMIBObjects=_StunMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,200,1))
class _StunEnable_Type(MxEnableState):defaultValue=0
_StunEnable_Type.__name__=_H
_StunEnable_Object=MibScalar
stunEnable=_StunEnable_Object((1,3,6,1,4,1,4935,15,200,1,50),_StunEnable_Type())
stunEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:stunEnable.setStatus(_A)
class _StunQueryCacheDuration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_StunQueryCacheDuration_Type.__name__=_C
_StunQueryCacheDuration_Object=MibScalar
stunQueryCacheDuration=_StunQueryCacheDuration_Object((1,3,6,1,4,1,4935,15,200,1,100),_StunQueryCacheDuration_Type())
stunQueryCacheDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:stunQueryCacheDuration.setStatus(_A)
class _StunQueryTimeout_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_StunQueryTimeout_Type.__name__=_C
_StunQueryTimeout_Object=MibScalar
stunQueryTimeout=_StunQueryTimeout_Object((1,3,6,1,4,1,4935,15,200,1,150),_StunQueryTimeout_Type())
stunQueryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:stunQueryTimeout.setStatus(_A)
class _StunKeepAliveInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_StunKeepAliveInterval_Type.__name__=_C
_StunKeepAliveInterval_Object=MibScalar
stunKeepAliveInterval=_StunKeepAliveInterval_Object((1,3,6,1,4,1,4935,15,200,1,200),_StunKeepAliveInterval_Type())
stunKeepAliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:stunKeepAliveInterval.setStatus(_A)
class _StunNatBindingQueryInterval_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,600))
_StunNatBindingQueryInterval_Type.__name__=_C
_StunNatBindingQueryInterval_Object=MibScalar
stunNatBindingQueryInterval=_StunNatBindingQueryInterval_Object((1,3,6,1,4,1,4935,15,200,1,250),_StunNatBindingQueryInterval_Type())
stunNatBindingQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:stunNatBindingQueryInterval.setStatus(_A)
_StunConformance_ObjectIdentity=ObjectIdentity
stunConformance=_StunConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,200,2))
_StunCompliances_ObjectIdentity=ObjectIdentity
stunCompliances=_StunCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,200,2,1))
_StunGroups_ObjectIdentity=ObjectIdentity
stunGroups=_StunGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,200,2,2))
stunBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,200,2,2,1))
stunBasicGroupVer1.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:stunBasicGroupVer1.setStatus(_A)
stunServerGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,200,2,2,2))
stunServerGroupVer1.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:stunServerGroupVer1.setStatus(_A)
stunComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,200,2,1,1))
stunComplVer1.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:stunComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusStun':ipAddressStatusStun,'stunTable':stunTable,'stunEntry':stunEntry,_I:stunIndex,_Q:stunHost,_R:stunPort,'ipAddressConfigStun':ipAddressConfigStun,'ipAddressConfigStunStatic':ipAddressConfigStunStatic,'stunStaticTable':stunStaticTable,'stunStaticEntry':stunStaticEntry,_K:stunStaticIndex,_S:stunStaticHost,_T:stunStaticPort,'stunMIB':stunMIB,'stunMIBObjects':stunMIBObjects,_L:stunEnable,_M:stunQueryCacheDuration,_N:stunQueryTimeout,_O:stunKeepAliveInterval,_P:stunNatBindingQueryInterval,'stunConformance':stunConformance,'stunCompliances':stunCompliances,'stunComplVer1':stunComplVer1,'stunGroups':stunGroups,_U:stunBasicGroupVer1,_V:stunServerGroupVer1})