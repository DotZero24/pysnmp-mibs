_I='not-accessible'
_H='adGenIGMPCacheIndex'
_G='adGenIGMPCacheAddress'
_F='Integer32'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='ADTRAN-GENIGMPCACHE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenIGMPCache,adGenIGMPCacheID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenIGMPCache','adGenIGMPCacheID')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenIGMPCacheMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,11,11))
if mibBuilder.loadTexts:adGenIGMPCacheMIB.setRevisions(('2013-03-05 00:00','2011-10-31 00:00','2011-10-28 00:00','2009-05-08 00:00'))
_AdGenIGMPCacheTable_Object=MibTable
adGenIGMPCacheTable=_AdGenIGMPCacheTable_Object((1,3,6,1,4,1,664,5,70,11,1))
if mibBuilder.loadTexts:adGenIGMPCacheTable.setStatus(_A)
_AdGenIGMPCacheEntry_Object=MibTableRow
adGenIGMPCacheEntry=_AdGenIGMPCacheEntry_Object((1,3,6,1,4,1,664,5,70,11,1,1))
adGenIGMPCacheEntry.setIndexNames((0,_D,_E),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:adGenIGMPCacheEntry.setStatus(_A)
_AdGenIGMPCacheAddress_Type=IpAddress
_AdGenIGMPCacheAddress_Object=MibTableColumn
adGenIGMPCacheAddress=_AdGenIGMPCacheAddress_Object((1,3,6,1,4,1,664,5,70,11,1,1,1),_AdGenIGMPCacheAddress_Type())
adGenIGMPCacheAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenIGMPCacheAddress.setStatus(_A)
_AdGenIGMPCacheIndex_Type=Integer32
_AdGenIGMPCacheIndex_Object=MibTableColumn
adGenIGMPCacheIndex=_AdGenIGMPCacheIndex_Object((1,3,6,1,4,1,664,5,70,11,1,1,2),_AdGenIGMPCacheIndex_Type())
adGenIGMPCacheIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenIGMPCacheIndex.setStatus(_A)
_AdGenIGMPCacheLastReporter_Type=IpAddress
_AdGenIGMPCacheLastReporter_Object=MibTableColumn
adGenIGMPCacheLastReporter=_AdGenIGMPCacheLastReporter_Object((1,3,6,1,4,1,664,5,70,11,1,1,3),_AdGenIGMPCacheLastReporter_Type())
adGenIGMPCacheLastReporter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheLastReporter.setStatus(_A)
_AdGenIGMPCacheUpTime_Type=TimeTicks
_AdGenIGMPCacheUpTime_Object=MibTableColumn
adGenIGMPCacheUpTime=_AdGenIGMPCacheUpTime_Object((1,3,6,1,4,1,664,5,70,11,1,1,4),_AdGenIGMPCacheUpTime_Type())
adGenIGMPCacheUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheUpTime.setStatus(_A)
_AdGenIGMPCacheExpiryTime_Type=TimeTicks
_AdGenIGMPCacheExpiryTime_Object=MibTableColumn
adGenIGMPCacheExpiryTime=_AdGenIGMPCacheExpiryTime_Object((1,3,6,1,4,1,664,5,70,11,1,1,5),_AdGenIGMPCacheExpiryTime_Type())
adGenIGMPCacheExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheExpiryTime.setStatus(_A)
_AdGenIGMPCacheInterfaceDescription_Type=DisplayString
_AdGenIGMPCacheInterfaceDescription_Object=MibTableColumn
adGenIGMPCacheInterfaceDescription=_AdGenIGMPCacheInterfaceDescription_Object((1,3,6,1,4,1,664,5,70,11,1,1,6),_AdGenIGMPCacheInterfaceDescription_Type())
adGenIGMPCacheInterfaceDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheInterfaceDescription.setStatus(_A)
_AdGenIGMPCacheInterfaceName_Type=DisplayString
_AdGenIGMPCacheInterfaceName_Object=MibTableColumn
adGenIGMPCacheInterfaceName=_AdGenIGMPCacheInterfaceName_Object((1,3,6,1,4,1,664,5,70,11,1,1,7),_AdGenIGMPCacheInterfaceName_Type())
adGenIGMPCacheInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheInterfaceName.setStatus(_A)
class _AdGenIGMPCacheMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v2',1),('v3lite',2),('v2Compatibility',3)))
_AdGenIGMPCacheMode_Type.__name__=_F
_AdGenIGMPCacheMode_Object=MibTableColumn
adGenIGMPCacheMode=_AdGenIGMPCacheMode_Object((1,3,6,1,4,1,664,5,70,11,1,1,8),_AdGenIGMPCacheMode_Type())
adGenIGMPCacheMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIGMPCacheMode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adGenIGMPCacheTable':adGenIGMPCacheTable,'adGenIGMPCacheEntry':adGenIGMPCacheEntry,_G:adGenIGMPCacheAddress,_H:adGenIGMPCacheIndex,'adGenIGMPCacheLastReporter':adGenIGMPCacheLastReporter,'adGenIGMPCacheUpTime':adGenIGMPCacheUpTime,'adGenIGMPCacheExpiryTime':adGenIGMPCacheExpiryTime,'adGenIGMPCacheInterfaceDescription':adGenIGMPCacheInterfaceDescription,'adGenIGMPCacheInterfaceName':adGenIGMPCacheInterfaceName,'adGenIGMPCacheMode':adGenIGMPCacheMode,'adGenIGMPCacheMIB':adGenIGMPCacheMIB})