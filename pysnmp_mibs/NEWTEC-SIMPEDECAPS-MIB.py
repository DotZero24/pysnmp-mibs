_O='ntcSiMpeDeConfGrpV1Standard'
_N='ntcSiMpeDeAlDataOverflow'
_M='ntcSiMpeDeDroppedPackets'
_L='ntcSiMpeDeForwardBitRate'
_K='ntcSiMpeDeCounterReset'
_J='ntcSiMpeDeMacAddress'
_I='ntcSiMpeDeDataPid'
_H='ntcSiMpeDeEnable'
_G='Unsigned32'
_F='Integer32'
_E='NtcEnable'
_D='read-only'
_C='read-write'
_B='NEWTEC-SIMPEDECAPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ntcSiMpeDecaps=ModuleIdentity((1,3,6,1,4,1,5835,5,2,8500))
if mibBuilder.loadTexts:ntcSiMpeDecaps.setRevisions(('2017-07-10 12:00','2014-09-09 09:00'))
_NtcSiMpeDeObjects_ObjectIdentity=ObjectIdentity
ntcSiMpeDeObjects=_NtcSiMpeDeObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,1))
if mibBuilder.loadTexts:ntcSiMpeDeObjects.setStatus(_A)
_NtcSiMpeDeConfiguration_ObjectIdentity=ObjectIdentity
ntcSiMpeDeConfiguration=_NtcSiMpeDeConfiguration_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,1,1))
if mibBuilder.loadTexts:ntcSiMpeDeConfiguration.setStatus(_A)
class _NtcSiMpeDeEnable_Type(NtcEnable):defaultValue=0
_NtcSiMpeDeEnable_Type.__name__=_E
_NtcSiMpeDeEnable_Object=MibScalar
ntcSiMpeDeEnable=_NtcSiMpeDeEnable_Object((1,3,6,1,4,1,5835,5,2,8500,1,1,1),_NtcSiMpeDeEnable_Type())
ntcSiMpeDeEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcSiMpeDeEnable.setStatus(_A)
class _NtcSiMpeDeDataPid_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,8190))
_NtcSiMpeDeDataPid_Type.__name__=_G
_NtcSiMpeDeDataPid_Object=MibScalar
ntcSiMpeDeDataPid=_NtcSiMpeDeDataPid_Object((1,3,6,1,4,1,5835,5,2,8500,1,1,2),_NtcSiMpeDeDataPid_Type())
ntcSiMpeDeDataPid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcSiMpeDeDataPid.setStatus(_A)
_NtcSiMpeDeMacAddress_Type=MacAddress
_NtcSiMpeDeMacAddress_Object=MibScalar
ntcSiMpeDeMacAddress=_NtcSiMpeDeMacAddress_Object((1,3,6,1,4,1,5835,5,2,8500,1,1,3),_NtcSiMpeDeMacAddress_Type())
ntcSiMpeDeMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcSiMpeDeMacAddress.setStatus(_A)
_NtcSiMpeDeMonitoring_ObjectIdentity=ObjectIdentity
ntcSiMpeDeMonitoring=_NtcSiMpeDeMonitoring_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,1,2))
if mibBuilder.loadTexts:ntcSiMpeDeMonitoring.setStatus(_A)
class _NtcSiMpeDeCounterReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcSiMpeDeCounterReset_Type.__name__=_F
_NtcSiMpeDeCounterReset_Object=MibScalar
ntcSiMpeDeCounterReset=_NtcSiMpeDeCounterReset_Object((1,3,6,1,4,1,5835,5,2,8500,1,2,1),_NtcSiMpeDeCounterReset_Type())
ntcSiMpeDeCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcSiMpeDeCounterReset.setStatus(_A)
_NtcSiMpeDeForwardBitRate_Type=Counter64
_NtcSiMpeDeForwardBitRate_Object=MibScalar
ntcSiMpeDeForwardBitRate=_NtcSiMpeDeForwardBitRate_Object((1,3,6,1,4,1,5835,5,2,8500,1,2,2),_NtcSiMpeDeForwardBitRate_Type())
ntcSiMpeDeForwardBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcSiMpeDeForwardBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcSiMpeDeForwardBitRate.setUnits('bps')
_NtcSiMpeDeDroppedPackets_Type=Counter64
_NtcSiMpeDeDroppedPackets_Object=MibScalar
ntcSiMpeDeDroppedPackets=_NtcSiMpeDeDroppedPackets_Object((1,3,6,1,4,1,5835,5,2,8500,1,2,3),_NtcSiMpeDeDroppedPackets_Type())
ntcSiMpeDeDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcSiMpeDeDroppedPackets.setStatus(_A)
if mibBuilder.loadTexts:ntcSiMpeDeDroppedPackets.setUnits('packets')
_NtcSiMpeDeAlarms_ObjectIdentity=ObjectIdentity
ntcSiMpeDeAlarms=_NtcSiMpeDeAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,1,3))
if mibBuilder.loadTexts:ntcSiMpeDeAlarms.setStatus(_A)
_NtcSiMpeDeAlDataOverflow_Type=NtcAlarmState
_NtcSiMpeDeAlDataOverflow_Object=MibScalar
ntcSiMpeDeAlDataOverflow=_NtcSiMpeDeAlDataOverflow_Object((1,3,6,1,4,1,5835,5,2,8500,1,3,1),_NtcSiMpeDeAlDataOverflow_Type())
ntcSiMpeDeAlDataOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcSiMpeDeAlDataOverflow.setStatus(_A)
_NtcSiMpeDeConformance_ObjectIdentity=ObjectIdentity
ntcSiMpeDeConformance=_NtcSiMpeDeConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,2))
if mibBuilder.loadTexts:ntcSiMpeDeConformance.setStatus(_A)
_NtcSiMpeDeConfCompliance_ObjectIdentity=ObjectIdentity
ntcSiMpeDeConfCompliance=_NtcSiMpeDeConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,2,1))
if mibBuilder.loadTexts:ntcSiMpeDeConfCompliance.setStatus(_A)
_NtcSiMpeDeConfGroup_ObjectIdentity=ObjectIdentity
ntcSiMpeDeConfGroup=_NtcSiMpeDeConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8500,2,2))
if mibBuilder.loadTexts:ntcSiMpeDeConfGroup.setStatus(_A)
ntcSiMpeDeConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,8500,2,2,1))
ntcSiMpeDeConfGrpV1Standard.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ntcSiMpeDeConfGrpV1Standard.setStatus(_A)
ntcSiMpeDeConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,8500,2,1,1))
ntcSiMpeDeConfCompV1Standard.setObjects((_B,_O))
if mibBuilder.loadTexts:ntcSiMpeDeConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcSiMpeDecaps':ntcSiMpeDecaps,'ntcSiMpeDeObjects':ntcSiMpeDeObjects,'ntcSiMpeDeConfiguration':ntcSiMpeDeConfiguration,_H:ntcSiMpeDeEnable,_I:ntcSiMpeDeDataPid,_J:ntcSiMpeDeMacAddress,'ntcSiMpeDeMonitoring':ntcSiMpeDeMonitoring,_K:ntcSiMpeDeCounterReset,_L:ntcSiMpeDeForwardBitRate,_M:ntcSiMpeDeDroppedPackets,'ntcSiMpeDeAlarms':ntcSiMpeDeAlarms,_N:ntcSiMpeDeAlDataOverflow,'ntcSiMpeDeConformance':ntcSiMpeDeConformance,'ntcSiMpeDeConfCompliance':ntcSiMpeDeConfCompliance,'ntcSiMpeDeConfCompV1Standard':ntcSiMpeDeConfCompV1Standard,'ntcSiMpeDeConfGroup':ntcSiMpeDeConfGroup,_O:ntcSiMpeDeConfGrpV1Standard})