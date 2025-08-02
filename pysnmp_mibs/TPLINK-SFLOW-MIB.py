_I='tpSflowCollectorCollectorId'
_H='TPLINK-SFLOW-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSflowMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,95))
if mibBuilder.loadTexts:tplinkSflowMIB.setRevisions(('2015-09-23 10:07',))
_TplinkSflowMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSflowMIBObjects=_TplinkSflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,95,1))
_TpSflowGlobalConfig_ObjectIdentity=ObjectIdentity
tpSflowGlobalConfig=_TpSflowGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,95,1,1))
class _TpSflowGlobalConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpSflowGlobalConfigStatus_Type.__name__=_C
_TpSflowGlobalConfigStatus_Object=MibScalar
tpSflowGlobalConfigStatus=_TpSflowGlobalConfigStatus_Object((1,3,6,1,4,1,11863,6,95,1,1,1),_TpSflowGlobalConfigStatus_Type())
tpSflowGlobalConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowGlobalConfigStatus.setStatus(_A)
_TpSflowGlobalConfigAddress_Type=IpAddress
_TpSflowGlobalConfigAddress_Object=MibScalar
tpSflowGlobalConfigAddress=_TpSflowGlobalConfigAddress_Object((1,3,6,1,4,1,11863,6,95,1,1,2),_TpSflowGlobalConfigAddress_Type())
tpSflowGlobalConfigAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowGlobalConfigAddress.setStatus(_A)
_TpSflowGlobalConfigVersion_Type=Integer32
_TpSflowGlobalConfigVersion_Object=MibScalar
tpSflowGlobalConfigVersion=_TpSflowGlobalConfigVersion_Object((1,3,6,1,4,1,11863,6,95,1,1,3),_TpSflowGlobalConfigVersion_Type())
tpSflowGlobalConfigVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSflowGlobalConfigVersion.setStatus(_A)
_TpSflowCollector_ObjectIdentity=ObjectIdentity
tpSflowCollector=_TpSflowCollector_ObjectIdentity((1,3,6,1,4,1,11863,6,95,1,2))
_TpSflowCollectorTable_Object=MibTable
tpSflowCollectorTable=_TpSflowCollectorTable_Object((1,3,6,1,4,1,11863,6,95,1,2,1))
if mibBuilder.loadTexts:tpSflowCollectorTable.setStatus(_A)
_TpSflowCollectorEntry_Object=MibTableRow
tpSflowCollectorEntry=_TpSflowCollectorEntry_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1))
tpSflowCollectorEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:tpSflowCollectorEntry.setStatus(_A)
_TpSflowCollectorCollectorId_Type=Integer32
_TpSflowCollectorCollectorId_Object=MibTableColumn
tpSflowCollectorCollectorId=_TpSflowCollectorCollectorId_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,1),_TpSflowCollectorCollectorId_Type())
tpSflowCollectorCollectorId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSflowCollectorCollectorId.setStatus(_A)
_TpSflowCollectorDescription_Type=DisplayString
_TpSflowCollectorDescription_Object=MibTableColumn
tpSflowCollectorDescription=_TpSflowCollectorDescription_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,2),_TpSflowCollectorDescription_Type())
tpSflowCollectorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowCollectorDescription.setStatus(_A)
_TpSflowCollectorCollectorIp_Type=IpAddress
_TpSflowCollectorCollectorIp_Object=MibTableColumn
tpSflowCollectorCollectorIp=_TpSflowCollectorCollectorIp_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,3),_TpSflowCollectorCollectorIp_Type())
tpSflowCollectorCollectorIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowCollectorCollectorIp.setStatus(_A)
class _TpSflowCollectorCollectorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpSflowCollectorCollectorPort_Type.__name__=_C
_TpSflowCollectorCollectorPort_Object=MibTableColumn
tpSflowCollectorCollectorPort=_TpSflowCollectorCollectorPort_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,4),_TpSflowCollectorCollectorPort_Type())
tpSflowCollectorCollectorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowCollectorCollectorPort.setStatus(_A)
class _TpSflowCollectorMaxDatagram_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1400))
_TpSflowCollectorMaxDatagram_Type.__name__=_C
_TpSflowCollectorMaxDatagram_Object=MibTableColumn
tpSflowCollectorMaxDatagram=_TpSflowCollectorMaxDatagram_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,5),_TpSflowCollectorMaxDatagram_Type())
tpSflowCollectorMaxDatagram.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowCollectorMaxDatagram.setStatus(_A)
class _TpSflowCollectorTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpSflowCollectorTimeout_Type.__name__=_C
_TpSflowCollectorTimeout_Object=MibTableColumn
tpSflowCollectorTimeout=_TpSflowCollectorTimeout_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,6),_TpSflowCollectorTimeout_Type())
tpSflowCollectorTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowCollectorTimeout.setStatus(_A)
_TpSflowCollectorLifetime_Type=Integer32
_TpSflowCollectorLifetime_Object=MibTableColumn
tpSflowCollectorLifetime=_TpSflowCollectorLifetime_Object((1,3,6,1,4,1,11863,6,95,1,2,1,1,7),_TpSflowCollectorLifetime_Type())
tpSflowCollectorLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSflowCollectorLifetime.setStatus(_A)
_TpSflowSampler_ObjectIdentity=ObjectIdentity
tpSflowSampler=_TpSflowSampler_ObjectIdentity((1,3,6,1,4,1,11863,6,95,1,3))
_TpSflowSamplerTable_Object=MibTable
tpSflowSamplerTable=_TpSflowSamplerTable_Object((1,3,6,1,4,1,11863,6,95,1,3,1))
if mibBuilder.loadTexts:tpSflowSamplerTable.setStatus(_A)
_TpSflowSamplerEntry_Object=MibTableRow
tpSflowSamplerEntry=_TpSflowSamplerEntry_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1))
tpSflowSamplerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpSflowSamplerEntry.setStatus(_A)
_TpSflowSamplerPort_Type=DisplayString
_TpSflowSamplerPort_Object=MibTableColumn
tpSflowSamplerPort=_TpSflowSamplerPort_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,1),_TpSflowSamplerPort_Type())
tpSflowSamplerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSflowSamplerPort.setStatus(_A)
class _TpSflowSamplerCollectorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_TpSflowSamplerCollectorId_Type.__name__=_C
_TpSflowSamplerCollectorId_Object=MibTableColumn
tpSflowSamplerCollectorId=_TpSflowSamplerCollectorId_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,2),_TpSflowSamplerCollectorId_Type())
tpSflowSamplerCollectorId.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowSamplerCollectorId.setStatus(_A)
class _TpSflowSamplerIngRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpSflowSamplerIngRate_Type.__name__=_C
_TpSflowSamplerIngRate_Object=MibTableColumn
tpSflowSamplerIngRate=_TpSflowSamplerIngRate_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,3),_TpSflowSamplerIngRate_Type())
tpSflowSamplerIngRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowSamplerIngRate.setStatus(_A)
class _TpSflowSamplerEgRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpSflowSamplerEgRate_Type.__name__=_C
_TpSflowSamplerEgRate_Object=MibTableColumn
tpSflowSamplerEgRate=_TpSflowSamplerEgRate_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,4),_TpSflowSamplerEgRate_Type())
tpSflowSamplerEgRate.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowSamplerEgRate.setStatus(_A)
class _TpSflowSamplerMaxHeader_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(18,256))
_TpSflowSamplerMaxHeader_Type.__name__=_C
_TpSflowSamplerMaxHeader_Object=MibTableColumn
tpSflowSamplerMaxHeader=_TpSflowSamplerMaxHeader_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,5),_TpSflowSamplerMaxHeader_Type())
tpSflowSamplerMaxHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSflowSamplerMaxHeader.setStatus(_A)
class _TpSflowSamplerPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpSflowSamplerPortLag_Type.__name__=_E
_TpSflowSamplerPortLag_Object=MibTableColumn
tpSflowSamplerPortLag=_TpSflowSamplerPortLag_Object((1,3,6,1,4,1,11863,6,95,1,3,1,1,6),_TpSflowSamplerPortLag_Type())
tpSflowSamplerPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpSflowSamplerPortLag.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'tplinkSflowMIB':tplinkSflowMIB,'tplinkSflowMIBObjects':tplinkSflowMIBObjects,'tpSflowGlobalConfig':tpSflowGlobalConfig,'tpSflowGlobalConfigStatus':tpSflowGlobalConfigStatus,'tpSflowGlobalConfigAddress':tpSflowGlobalConfigAddress,'tpSflowGlobalConfigVersion':tpSflowGlobalConfigVersion,'tpSflowCollector':tpSflowCollector,'tpSflowCollectorTable':tpSflowCollectorTable,'tpSflowCollectorEntry':tpSflowCollectorEntry,_I:tpSflowCollectorCollectorId,'tpSflowCollectorDescription':tpSflowCollectorDescription,'tpSflowCollectorCollectorIp':tpSflowCollectorCollectorIp,'tpSflowCollectorCollectorPort':tpSflowCollectorCollectorPort,'tpSflowCollectorMaxDatagram':tpSflowCollectorMaxDatagram,'tpSflowCollectorTimeout':tpSflowCollectorTimeout,'tpSflowCollectorLifetime':tpSflowCollectorLifetime,'tpSflowSampler':tpSflowSampler,'tpSflowSamplerTable':tpSflowSamplerTable,'tpSflowSamplerEntry':tpSflowSamplerEntry,'tpSflowSamplerPort':tpSflowSamplerPort,'tpSflowSamplerCollectorId':tpSflowSamplerCollectorId,'tpSflowSamplerIngRate':tpSflowSamplerIngRate,'tpSflowSamplerEgRate':tpSflowSamplerEgRate,'tpSflowSamplerMaxHeader':tpSflowSamplerMaxHeader,'tpSflowSamplerPortLag':tpSflowSamplerPortLag})