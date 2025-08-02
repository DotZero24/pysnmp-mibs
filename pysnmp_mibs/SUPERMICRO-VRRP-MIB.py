_H='fsVrrpOperEntry'
_G='SUPERMICRO-VRRP-MIB'
_F='read-create'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vrrpOperEntry,=mibBuilder.importSymbols('VRRP-MIB','vrrpOperEntry')
fsvrrp=ModuleIdentity((1,3,6,1,4,1,10876,101,1,153))
if mibBuilder.loadTexts:fsvrrp.setRevisions(('2012-09-05 00:00',))
_FsVrrpSystem_ObjectIdentity=ObjectIdentity
fsVrrpSystem=_FsVrrpSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,1,153,1))
class _FsVrrpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsVrrpStatus_Type.__name__=_B
_FsVrrpStatus_Object=MibScalar
fsVrrpStatus=_FsVrrpStatus_Object((1,3,6,1,4,1,10876,101,1,153,1,1),_FsVrrpStatus_Type())
fsVrrpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpStatus.setStatus(_A)
_FsVrrpMaxOperEntries_Type=Integer32
_FsVrrpMaxOperEntries_Object=MibScalar
fsVrrpMaxOperEntries=_FsVrrpMaxOperEntries_Object((1,3,6,1,4,1,10876,101,1,153,1,2),_FsVrrpMaxOperEntries_Type())
fsVrrpMaxOperEntries.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsVrrpMaxOperEntries.setStatus(_A)
_FsVrrpOperTable_Object=MibTable
fsVrrpOperTable=_FsVrrpOperTable_Object((1,3,6,1,4,1,10876,101,1,153,1,3))
if mibBuilder.loadTexts:fsVrrpOperTable.setStatus(_A)
_FsVrrpOperEntry_Object=MibTableRow
fsVrrpOperEntry=_FsVrrpOperEntry_Object((1,3,6,1,4,1,10876,101,1,153,1,3,1))
if mibBuilder.loadTexts:fsVrrpOperEntry.setStatus(_A)
class _FsVrrpAdminPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_FsVrrpAdminPriority_Type.__name__=_B
_FsVrrpAdminPriority_Object=MibTableColumn
fsVrrpAdminPriority=_FsVrrpAdminPriority_Object((1,3,6,1,4,1,10876,101,1,153,1,3,1,1),_FsVrrpAdminPriority_Type())
fsVrrpAdminPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpAdminPriority.setStatus(_A)
class _FsVrrpOperAdvertisementIntervalInMsec_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,255000))
_FsVrrpOperAdvertisementIntervalInMsec_Type.__name__=_B
_FsVrrpOperAdvertisementIntervalInMsec_Object=MibTableColumn
fsVrrpOperAdvertisementIntervalInMsec=_FsVrrpOperAdvertisementIntervalInMsec_Object((1,3,6,1,4,1,10876,101,1,153,1,3,1,2),_FsVrrpOperAdvertisementIntervalInMsec_Type())
fsVrrpOperAdvertisementIntervalInMsec.setMaxAccess(_F)
if mibBuilder.loadTexts:fsVrrpOperAdvertisementIntervalInMsec.setStatus(_A)
if mibBuilder.loadTexts:fsVrrpOperAdvertisementIntervalInMsec.setUnits('milli seconds')
class _FsvrrpOperPingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsvrrpOperPingEnable_Type.__name__=_B
_FsvrrpOperPingEnable_Object=MibTableColumn
fsvrrpOperPingEnable=_FsvrrpOperPingEnable_Object((1,3,6,1,4,1,10876,101,1,153,1,3,1,3),_FsvrrpOperPingEnable_Type())
fsvrrpOperPingEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:fsvrrpOperPingEnable.setStatus(_A)
class _FsVrrpAuthDeprecate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsVrrpAuthDeprecate_Type.__name__=_B
_FsVrrpAuthDeprecate_Object=MibScalar
fsVrrpAuthDeprecate=_FsVrrpAuthDeprecate_Object((1,3,6,1,4,1,10876,101,1,153,1,4),_FsVrrpAuthDeprecate_Type())
fsVrrpAuthDeprecate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpAuthDeprecate.setStatus(_A)
class _FsVrrpTraceOption_Type(Integer32):defaultValue=0
_FsVrrpTraceOption_Type.__name__=_B
_FsVrrpTraceOption_Object=MibScalar
fsVrrpTraceOption=_FsVrrpTraceOption_Object((1,3,6,1,4,1,10876,101,1,153,1,5),_FsVrrpTraceOption_Type())
fsVrrpTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVrrpTraceOption.setStatus(_A)
vrrpOperEntry.registerAugmentions((_G,_H))
fsVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{'fsvrrp':fsvrrp,'fsVrrpSystem':fsVrrpSystem,'fsVrrpStatus':fsVrrpStatus,'fsVrrpMaxOperEntries':fsVrrpMaxOperEntries,'fsVrrpOperTable':fsVrrpOperTable,_H:fsVrrpOperEntry,'fsVrrpAdminPriority':fsVrrpAdminPriority,'fsVrrpOperAdvertisementIntervalInMsec':fsVrrpOperAdvertisementIntervalInMsec,'fsvrrpOperPingEnable':fsvrrpOperPingEnable,'fsVrrpAuthDeprecate':fsVrrpAuthDeprecate,'fsVrrpTraceOption':fsVrrpTraceOption})