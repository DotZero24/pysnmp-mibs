_M='pppBridgeMediaConfigMacType'
_L='pppBridgeMediaMacType'
_K='dont-accept'
_J='accept'
_I='PPP-BRIDGE-NCP-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='read-write'
_E='true'
_D='false'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ppp,=mibBuilder.importSymbols('PPP-LCP-MIB','ppp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_PppBridge_ObjectIdentity=ObjectIdentity
pppBridge=_PppBridge_ObjectIdentity((1,3,6,1,2,1,10,23,4))
_PppBridgeTable_Object=MibTable
pppBridgeTable=_PppBridgeTable_Object((1,3,6,1,2,1,10,23,4,1))
if mibBuilder.loadTexts:pppBridgeTable.setStatus(_A)
_PppBridgeEntry_Object=MibTableRow
pppBridgeEntry=_PppBridgeEntry_Object((1,3,6,1,2,1,10,23,4,1,1))
pppBridgeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pppBridgeEntry.setStatus(_A)
class _PppBridgeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('opened',1),('not-opened',2)))
_PppBridgeOperStatus_Type.__name__=_B
_PppBridgeOperStatus_Object=MibTableColumn
pppBridgeOperStatus=_PppBridgeOperStatus_Object((1,3,6,1,2,1,10,23,4,1,1,1),_PppBridgeOperStatus_Type())
pppBridgeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeOperStatus.setStatus(_A)
class _PppBridgeLocalToRemoteTinygramCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeLocalToRemoteTinygramCompression_Type.__name__=_B
_PppBridgeLocalToRemoteTinygramCompression_Object=MibTableColumn
pppBridgeLocalToRemoteTinygramCompression=_PppBridgeLocalToRemoteTinygramCompression_Object((1,3,6,1,2,1,10,23,4,1,1,2),_PppBridgeLocalToRemoteTinygramCompression_Type())
pppBridgeLocalToRemoteTinygramCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeLocalToRemoteTinygramCompression.setStatus(_A)
class _PppBridgeRemoteToLocalTinygramCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeRemoteToLocalTinygramCompression_Type.__name__=_B
_PppBridgeRemoteToLocalTinygramCompression_Object=MibTableColumn
pppBridgeRemoteToLocalTinygramCompression=_PppBridgeRemoteToLocalTinygramCompression_Object((1,3,6,1,2,1,10,23,4,1,1,3),_PppBridgeRemoteToLocalTinygramCompression_Type())
pppBridgeRemoteToLocalTinygramCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeRemoteToLocalTinygramCompression.setStatus(_A)
class _PppBridgeLocalToRemoteLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeLocalToRemoteLanId_Type.__name__=_B
_PppBridgeLocalToRemoteLanId_Object=MibTableColumn
pppBridgeLocalToRemoteLanId=_PppBridgeLocalToRemoteLanId_Object((1,3,6,1,2,1,10,23,4,1,1,4),_PppBridgeLocalToRemoteLanId_Type())
pppBridgeLocalToRemoteLanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeLocalToRemoteLanId.setStatus(_A)
class _PppBridgeRemoteToLocalLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeRemoteToLocalLanId_Type.__name__=_B
_PppBridgeRemoteToLocalLanId_Object=MibTableColumn
pppBridgeRemoteToLocalLanId=_PppBridgeRemoteToLocalLanId_Object((1,3,6,1,2,1,10,23,4,1,1,5),_PppBridgeRemoteToLocalLanId_Type())
pppBridgeRemoteToLocalLanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeRemoteToLocalLanId.setStatus(_A)
_PppBridgeConfigTable_Object=MibTable
pppBridgeConfigTable=_PppBridgeConfigTable_Object((1,3,6,1,2,1,10,23,4,2))
if mibBuilder.loadTexts:pppBridgeConfigTable.setStatus(_A)
_PppBridgeConfigEntry_Object=MibTableRow
pppBridgeConfigEntry=_PppBridgeConfigEntry_Object((1,3,6,1,2,1,10,23,4,2,1))
pppBridgeConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pppBridgeConfigEntry.setStatus(_A)
class _PppBridgeConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
_PppBridgeConfigAdminStatus_Type.__name__=_B
_PppBridgeConfigAdminStatus_Object=MibTableColumn
pppBridgeConfigAdminStatus=_PppBridgeConfigAdminStatus_Object((1,3,6,1,2,1,10,23,4,2,1,1),_PppBridgeConfigAdminStatus_Type())
pppBridgeConfigAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeConfigAdminStatus.setStatus(_A)
class _PppBridgeConfigTinygram_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeConfigTinygram_Type.__name__=_B
_PppBridgeConfigTinygram_Object=MibTableColumn
pppBridgeConfigTinygram=_PppBridgeConfigTinygram_Object((1,3,6,1,2,1,10,23,4,2,1,2),_PppBridgeConfigTinygram_Type())
pppBridgeConfigTinygram.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeConfigTinygram.setStatus(_A)
class _PppBridgeConfigRingId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeConfigRingId_Type.__name__=_B
_PppBridgeConfigRingId_Object=MibTableColumn
pppBridgeConfigRingId=_PppBridgeConfigRingId_Object((1,3,6,1,2,1,10,23,4,2,1,3),_PppBridgeConfigRingId_Type())
pppBridgeConfigRingId.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeConfigRingId.setStatus(_A)
class _PppBridgeConfigLineId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeConfigLineId_Type.__name__=_B
_PppBridgeConfigLineId_Object=MibTableColumn
pppBridgeConfigLineId=_PppBridgeConfigLineId_Object((1,3,6,1,2,1,10,23,4,2,1,4),_PppBridgeConfigLineId_Type())
pppBridgeConfigLineId.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeConfigLineId.setStatus(_A)
class _PppBridgeConfigLanId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_PppBridgeConfigLanId_Type.__name__=_B
_PppBridgeConfigLanId_Object=MibTableColumn
pppBridgeConfigLanId=_PppBridgeConfigLanId_Object((1,3,6,1,2,1,10,23,4,2,1,5),_PppBridgeConfigLanId_Type())
pppBridgeConfigLanId.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeConfigLanId.setStatus(_A)
_PppBridgeMediaTable_Object=MibTable
pppBridgeMediaTable=_PppBridgeMediaTable_Object((1,3,6,1,2,1,10,23,4,3))
if mibBuilder.loadTexts:pppBridgeMediaTable.setStatus(_A)
_PppBridgeMediaEntry_Object=MibTableRow
pppBridgeMediaEntry=_PppBridgeMediaEntry_Object((1,3,6,1,2,1,10,23,4,3,1))
pppBridgeMediaEntry.setIndexNames((0,_G,_H),(0,_I,_L))
if mibBuilder.loadTexts:pppBridgeMediaEntry.setStatus(_A)
class _PppBridgeMediaMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppBridgeMediaMacType_Type.__name__=_B
_PppBridgeMediaMacType_Object=MibTableColumn
pppBridgeMediaMacType=_PppBridgeMediaMacType_Object((1,3,6,1,2,1,10,23,4,3,1,1),_PppBridgeMediaMacType_Type())
pppBridgeMediaMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeMediaMacType.setStatus(_A)
class _PppBridgeMediaLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PppBridgeMediaLocalStatus_Type.__name__=_B
_PppBridgeMediaLocalStatus_Object=MibTableColumn
pppBridgeMediaLocalStatus=_PppBridgeMediaLocalStatus_Object((1,3,6,1,2,1,10,23,4,3,1,2),_PppBridgeMediaLocalStatus_Type())
pppBridgeMediaLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeMediaLocalStatus.setStatus(_A)
class _PppBridgeMediaRemoteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PppBridgeMediaRemoteStatus_Type.__name__=_B
_PppBridgeMediaRemoteStatus_Object=MibTableColumn
pppBridgeMediaRemoteStatus=_PppBridgeMediaRemoteStatus_Object((1,3,6,1,2,1,10,23,4,3,1,3),_PppBridgeMediaRemoteStatus_Type())
pppBridgeMediaRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pppBridgeMediaRemoteStatus.setStatus(_A)
_PppBridgeMediaConfigTable_Object=MibTable
pppBridgeMediaConfigTable=_PppBridgeMediaConfigTable_Object((1,3,6,1,2,1,10,23,4,4))
if mibBuilder.loadTexts:pppBridgeMediaConfigTable.setStatus(_A)
_PppBridgeMediaConfigEntry_Object=MibTableRow
pppBridgeMediaConfigEntry=_PppBridgeMediaConfigEntry_Object((1,3,6,1,2,1,10,23,4,4,1))
pppBridgeMediaConfigEntry.setIndexNames((0,_G,_H),(0,_I,_M))
if mibBuilder.loadTexts:pppBridgeMediaConfigEntry.setStatus(_A)
class _PppBridgeMediaConfigMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppBridgeMediaConfigMacType_Type.__name__=_B
_PppBridgeMediaConfigMacType_Object=MibTableColumn
pppBridgeMediaConfigMacType=_PppBridgeMediaConfigMacType_Object((1,3,6,1,2,1,10,23,4,4,1,1),_PppBridgeMediaConfigMacType_Type())
pppBridgeMediaConfigMacType.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeMediaConfigMacType.setStatus(_A)
class _PppBridgeMediaConfigLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_PppBridgeMediaConfigLocalStatus_Type.__name__=_B
_PppBridgeMediaConfigLocalStatus_Object=MibTableColumn
pppBridgeMediaConfigLocalStatus=_PppBridgeMediaConfigLocalStatus_Object((1,3,6,1,2,1,10,23,4,4,1,2),_PppBridgeMediaConfigLocalStatus_Type())
pppBridgeMediaConfigLocalStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pppBridgeMediaConfigLocalStatus.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'pppBridge':pppBridge,'pppBridgeTable':pppBridgeTable,'pppBridgeEntry':pppBridgeEntry,'pppBridgeOperStatus':pppBridgeOperStatus,'pppBridgeLocalToRemoteTinygramCompression':pppBridgeLocalToRemoteTinygramCompression,'pppBridgeRemoteToLocalTinygramCompression':pppBridgeRemoteToLocalTinygramCompression,'pppBridgeLocalToRemoteLanId':pppBridgeLocalToRemoteLanId,'pppBridgeRemoteToLocalLanId':pppBridgeRemoteToLocalLanId,'pppBridgeConfigTable':pppBridgeConfigTable,'pppBridgeConfigEntry':pppBridgeConfigEntry,'pppBridgeConfigAdminStatus':pppBridgeConfigAdminStatus,'pppBridgeConfigTinygram':pppBridgeConfigTinygram,'pppBridgeConfigRingId':pppBridgeConfigRingId,'pppBridgeConfigLineId':pppBridgeConfigLineId,'pppBridgeConfigLanId':pppBridgeConfigLanId,'pppBridgeMediaTable':pppBridgeMediaTable,'pppBridgeMediaEntry':pppBridgeMediaEntry,_L:pppBridgeMediaMacType,'pppBridgeMediaLocalStatus':pppBridgeMediaLocalStatus,'pppBridgeMediaRemoteStatus':pppBridgeMediaRemoteStatus,'pppBridgeMediaConfigTable':pppBridgeMediaConfigTable,'pppBridgeMediaConfigEntry':pppBridgeMediaConfigEntry,_M:pppBridgeMediaConfigMacType,'pppBridgeMediaConfigLocalStatus':pppBridgeMediaConfigLocalStatus})