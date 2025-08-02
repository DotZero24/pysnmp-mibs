_G='nsSetSnmpCommHostIndex'
_F='NETSCREEN-SET-SNMP-MIB'
_E='yes'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenSetSnmpMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,9))
if mibBuilder.loadTexts:netscreenSetSnmpMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetSNMP_ObjectIdentity=ObjectIdentity
nsSetSNMP=_NsSetSNMP_ObjectIdentity((1,3,6,1,4,1,3224,7,9))
class _NsSetSnmpSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetSnmpSysName_Type.__name__=_D
_NsSetSnmpSysName_Object=MibScalar
nsSetSnmpSysName=_NsSetSnmpSysName_Object((1,3,6,1,4,1,3224,7,9,1),_NsSetSnmpSysName_Type())
nsSetSnmpSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpSysName.setStatus(_A)
class _NsSetSnmpContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetSnmpContact_Type.__name__=_D
_NsSetSnmpContact_Object=MibScalar
nsSetSnmpContact=_NsSetSnmpContact_Object((1,3,6,1,4,1,3224,7,9,2),_NsSetSnmpContact_Type())
nsSetSnmpContact.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpContact.setStatus(_A)
class _NsSetSnmpLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsSetSnmpLocation_Type.__name__=_D
_NsSetSnmpLocation_Object=MibScalar
nsSetSnmpLocation=_NsSetSnmpLocation_Object((1,3,6,1,4,1,3224,7,9,3),_NsSetSnmpLocation_Type())
nsSetSnmpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpLocation.setStatus(_A)
class _NsSetSnmpVPNEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsSetSnmpVPNEnable_Type.__name__=_C
_NsSetSnmpVPNEnable_Object=MibScalar
nsSetSnmpVPNEnable=_NsSetSnmpVPNEnable_Object((1,3,6,1,4,1,3224,7,9,4),_NsSetSnmpVPNEnable_Type())
nsSetSnmpVPNEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpVPNEnable.setStatus(_A)
_NsSetSnmpCommHostTable_Object=MibTable
nsSetSnmpCommHostTable=_NsSetSnmpCommHostTable_Object((1,3,6,1,4,1,3224,7,9,5))
if mibBuilder.loadTexts:nsSetSnmpCommHostTable.setStatus(_A)
_NsSetSnmpCommHostEntry_Object=MibTableRow
nsSetSnmpCommHostEntry=_NsSetSnmpCommHostEntry_Object((1,3,6,1,4,1,3224,7,9,5,1))
nsSetSnmpCommHostEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:nsSetSnmpCommHostEntry.setStatus(_A)
class _NsSetSnmpCommHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSetSnmpCommHostIndex_Type.__name__=_C
_NsSetSnmpCommHostIndex_Object=MibTableColumn
nsSetSnmpCommHostIndex=_NsSetSnmpCommHostIndex_Object((1,3,6,1,4,1,3224,7,9,5,1,1),_NsSetSnmpCommHostIndex_Type())
nsSetSnmpCommHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpCommHostIndex.setStatus(_A)
class _NsSetSnmpCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSetSnmpCommunity_Type.__name__=_D
_NsSetSnmpCommunity_Object=MibTableColumn
nsSetSnmpCommunity=_NsSetSnmpCommunity_Object((1,3,6,1,4,1,3224,7,9,5,1,2),_NsSetSnmpCommunity_Type())
nsSetSnmpCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpCommunity.setStatus(_A)
_NsSetSnmpHostInComm_Type=IpAddress
_NsSetSnmpHostInComm_Object=MibTableColumn
nsSetSnmpHostInComm=_NsSetSnmpHostInComm_Object((1,3,6,1,4,1,3224,7,9,5,1,3),_NsSetSnmpHostInComm_Type())
nsSetSnmpHostInComm.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpHostInComm.setStatus(_A)
class _NsSetSnmpWritePermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_E,1)))
_NsSetSnmpWritePermit_Type.__name__=_C
_NsSetSnmpWritePermit_Object=MibTableColumn
nsSetSnmpWritePermit=_NsSetSnmpWritePermit_Object((1,3,6,1,4,1,3224,7,9,5,1,4),_NsSetSnmpWritePermit_Type())
nsSetSnmpWritePermit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpWritePermit.setStatus(_A)
class _NsSetSnmpTrapPermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_E,1)))
_NsSetSnmpTrapPermit_Type.__name__=_C
_NsSetSnmpTrapPermit_Object=MibTableColumn
nsSetSnmpTrapPermit=_NsSetSnmpTrapPermit_Object((1,3,6,1,4,1,3224,7,9,5,1,5),_NsSetSnmpTrapPermit_Type())
nsSetSnmpTrapPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpTrapPermit.setStatus(_A)
class _NsSetSnmpTrafficAlarmPermit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_E,1)))
_NsSetSnmpTrafficAlarmPermit_Type.__name__=_C
_NsSetSnmpTrafficAlarmPermit_Object=MibTableColumn
nsSetSnmpTrafficAlarmPermit=_NsSetSnmpTrafficAlarmPermit_Object((1,3,6,1,4,1,3224,7,9,5,1,6),_NsSetSnmpTrafficAlarmPermit_Type())
nsSetSnmpTrafficAlarmPermit.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSetSnmpTrafficAlarmPermit.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'netscreenSetSnmpMibModule':netscreenSetSnmpMibModule,'nsSetSNMP':nsSetSNMP,'nsSetSnmpSysName':nsSetSnmpSysName,'nsSetSnmpContact':nsSetSnmpContact,'nsSetSnmpLocation':nsSetSnmpLocation,'nsSetSnmpVPNEnable':nsSetSnmpVPNEnable,'nsSetSnmpCommHostTable':nsSetSnmpCommHostTable,'nsSetSnmpCommHostEntry':nsSetSnmpCommHostEntry,_G:nsSetSnmpCommHostIndex,'nsSetSnmpCommunity':nsSetSnmpCommunity,'nsSetSnmpHostInComm':nsSetSnmpHostInComm,'nsSetSnmpWritePermit':nsSetSnmpWritePermit,'nsSetSnmpTrapPermit':nsSetSnmpTrapPermit,'nsSetSnmpTrafficAlarmPermit':nsSetSnmpTrafficAlarmPermit})