_I='trustful'
_H='untrusty'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkArpInspectionMIBObjects,=mibBuilder.importSymbols('TPLINK-ARP-INSPECTION-MIB','tplinkArpInspectionMIBObjects')
_TpArpDetection_ObjectIdentity=ObjectIdentity
tpArpDetection=_TpArpDetection_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,1))
_TpArpDetectionConfig_ObjectIdentity=ObjectIdentity
tpArpDetectionConfig=_TpArpDetectionConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,1,1))
class _TpArpDetectionConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpArpDetectionConfigEnable_Type.__name__=_B
_TpArpDetectionConfigEnable_Object=MibScalar
tpArpDetectionConfigEnable=_TpArpDetectionConfigEnable_Object((1,3,6,1,4,1,11863,6,28,1,1,1,1),_TpArpDetectionConfigEnable_Type())
tpArpDetectionConfigEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:tpArpDetectionConfigEnable.setStatus(_A)
_TpArpDetectionTrustPortTable_Object=MibTable
tpArpDetectionTrustPortTable=_TpArpDetectionTrustPortTable_Object((1,3,6,1,4,1,11863,6,28,1,1,1,2))
if mibBuilder.loadTexts:tpArpDetectionTrustPortTable.setStatus(_A)
_TpArpDetectionTrustPortEntry_Object=MibTableRow
tpArpDetectionTrustPortEntry=_TpArpDetectionTrustPortEntry_Object((1,3,6,1,4,1,11863,6,28,1,1,1,2,1))
tpArpDetectionTrustPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpArpDetectionTrustPortEntry.setStatus(_A)
_TpArpDetectionTrustPort_Type=OctetString
_TpArpDetectionTrustPort_Object=MibTableColumn
tpArpDetectionTrustPort=_TpArpDetectionTrustPort_Object((1,3,6,1,4,1,11863,6,28,1,1,1,2,1,1),_TpArpDetectionTrustPort_Type())
tpArpDetectionTrustPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpArpDetectionTrustPort.setStatus(_A)
class _TpArpDetectionTrustPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpArpDetectionTrustPortState_Type.__name__=_B
_TpArpDetectionTrustPortState_Object=MibTableColumn
tpArpDetectionTrustPortState=_TpArpDetectionTrustPortState_Object((1,3,6,1,4,1,11863,6,28,1,1,1,2,1,2),_TpArpDetectionTrustPortState_Type())
tpArpDetectionTrustPortState.setMaxAccess(_G)
if mibBuilder.loadTexts:tpArpDetectionTrustPortState.setStatus(_A)
class _TpArpDetectionTrustPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpArpDetectionTrustPortLag_Type.__name__=_D
_TpArpDetectionTrustPortLag_Object=MibTableColumn
tpArpDetectionTrustPortLag=_TpArpDetectionTrustPortLag_Object((1,3,6,1,4,1,11863,6,28,1,1,1,2,1,3),_TpArpDetectionTrustPortLag_Type())
tpArpDetectionTrustPortLag.setMaxAccess(_C)
if mibBuilder.loadTexts:tpArpDetectionTrustPortLag.setStatus(_A)
_TpArpDetectionStat_ObjectIdentity=ObjectIdentity
tpArpDetectionStat=_TpArpDetectionStat_ObjectIdentity((1,3,6,1,4,1,11863,6,28,1,1,2))
class _TpArpDetectionStatReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notReset',0),('reset',1)))
_TpArpDetectionStatReset_Type.__name__=_B
_TpArpDetectionStatReset_Object=MibScalar
tpArpDetectionStatReset=_TpArpDetectionStatReset_Object((1,3,6,1,4,1,11863,6,28,1,1,2,1),_TpArpDetectionStatReset_Type())
tpArpDetectionStatReset.setMaxAccess(_G)
if mibBuilder.loadTexts:tpArpDetectionStatReset.setStatus(_A)
_TpArpDetectionStatTable_Object=MibTable
tpArpDetectionStatTable=_TpArpDetectionStatTable_Object((1,3,6,1,4,1,11863,6,28,1,1,2,2))
if mibBuilder.loadTexts:tpArpDetectionStatTable.setStatus(_A)
_TpArpDetectionStatEntry_Object=MibTableRow
tpArpDetectionStatEntry=_TpArpDetectionStatEntry_Object((1,3,6,1,4,1,11863,6,28,1,1,2,2,1))
tpArpDetectionStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:tpArpDetectionStatEntry.setStatus(_A)
class _TpArpDetectionStatPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpArpDetectionStatPort_Type.__name__=_D
_TpArpDetectionStatPort_Object=MibTableColumn
tpArpDetectionStatPort=_TpArpDetectionStatPort_Object((1,3,6,1,4,1,11863,6,28,1,1,2,2,1,1),_TpArpDetectionStatPort_Type())
tpArpDetectionStatPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tpArpDetectionStatPort.setStatus(_A)
class _TpArpDetectionStatState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpArpDetectionStatState_Type.__name__=_B
_TpArpDetectionStatState_Object=MibTableColumn
tpArpDetectionStatState=_TpArpDetectionStatState_Object((1,3,6,1,4,1,11863,6,28,1,1,2,2,1,2),_TpArpDetectionStatState_Type())
tpArpDetectionStatState.setMaxAccess(_C)
if mibBuilder.loadTexts:tpArpDetectionStatState.setStatus(_A)
_TpArpDetectionStatNonLegalPkt_Type=Counter32
_TpArpDetectionStatNonLegalPkt_Object=MibTableColumn
tpArpDetectionStatNonLegalPkt=_TpArpDetectionStatNonLegalPkt_Object((1,3,6,1,4,1,11863,6,28,1,1,2,2,1,3),_TpArpDetectionStatNonLegalPkt_Type())
tpArpDetectionStatNonLegalPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:tpArpDetectionStatNonLegalPkt.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-ARP-DETECTION-MIB',**{'tpArpDetection':tpArpDetection,'tpArpDetectionConfig':tpArpDetectionConfig,'tpArpDetectionConfigEnable':tpArpDetectionConfigEnable,'tpArpDetectionTrustPortTable':tpArpDetectionTrustPortTable,'tpArpDetectionTrustPortEntry':tpArpDetectionTrustPortEntry,'tpArpDetectionTrustPort':tpArpDetectionTrustPort,'tpArpDetectionTrustPortState':tpArpDetectionTrustPortState,'tpArpDetectionTrustPortLag':tpArpDetectionTrustPortLag,'tpArpDetectionStat':tpArpDetectionStat,'tpArpDetectionStatReset':tpArpDetectionStatReset,'tpArpDetectionStatTable':tpArpDetectionStatTable,'tpArpDetectionStatEntry':tpArpDetectionStatEntry,'tpArpDetectionStatPort':tpArpDetectionStatPort,'tpArpDetectionStatState':tpArpDetectionStatState,'tpArpDetectionStatNonLegalPkt':tpArpDetectionStatNonLegalPkt})