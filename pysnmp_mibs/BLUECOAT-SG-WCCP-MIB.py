_F='deviceWccpIndex'
_E='BLUECOAT-SG-WCCP-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
deviceWccpMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,5))
if mibBuilder.loadTexts:deviceWccpMIB.setRevisions(('2008-01-23 03:00','2007-11-05 03:00','2002-08-28 03:00'))
class WccpServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standard',1),('dynamic',2),(_D,3)))
class WccpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version2',2),(_D,3)))
_DeviceWccpEnabled_Type=TruthValue
_DeviceWccpEnabled_Object=MibScalar
deviceWccpEnabled=_DeviceWccpEnabled_Object((1,3,6,1,4,1,3417,2,5,1),_DeviceWccpEnabled_Type())
deviceWccpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpEnabled.setStatus(_A)
_DeviceWccpMIBObjects_ObjectIdentity=ObjectIdentity
deviceWccpMIBObjects=_DeviceWccpMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,5,2))
_DeviceWccpValues_ObjectIdentity=ObjectIdentity
deviceWccpValues=_DeviceWccpValues_ObjectIdentity((1,3,6,1,4,1,3417,2,5,2,1))
_DeviceWccpValueTable_Object=MibTable
deviceWccpValueTable=_DeviceWccpValueTable_Object((1,3,6,1,4,1,3417,2,5,2,1,1))
if mibBuilder.loadTexts:deviceWccpValueTable.setStatus(_A)
_DeviceWccpValueEntry_Object=MibTableRow
deviceWccpValueEntry=_DeviceWccpValueEntry_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1))
deviceWccpValueEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:deviceWccpValueEntry.setStatus(_A)
class _DeviceWccpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceWccpIndex_Type.__name__=_C
_DeviceWccpIndex_Object=MibTableColumn
deviceWccpIndex=_DeviceWccpIndex_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,1),_DeviceWccpIndex_Type())
deviceWccpIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:deviceWccpIndex.setStatus(_A)
_DeviceWccpServiceID_Type=Integer32
_DeviceWccpServiceID_Object=MibTableColumn
deviceWccpServiceID=_DeviceWccpServiceID_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,2),_DeviceWccpServiceID_Type())
deviceWccpServiceID.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpServiceID.setStatus(_A)
_DeviceWccpServiceType_Type=WccpServiceType
_DeviceWccpServiceType_Object=MibTableColumn
deviceWccpServiceType=_DeviceWccpServiceType_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,3),_DeviceWccpServiceType_Type())
deviceWccpServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpServiceType.setStatus(_A)
_DeviceWccpServiceVersion_Type=WccpVersion
_DeviceWccpServiceVersion_Object=MibTableColumn
deviceWccpServiceVersion=_DeviceWccpServiceVersion_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,4),_DeviceWccpServiceVersion_Type())
deviceWccpServiceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpServiceVersion.setStatus(_A)
_DeviceWccpPacketsRedir_Type=Counter64
_DeviceWccpPacketsRedir_Object=MibTableColumn
deviceWccpPacketsRedir=_DeviceWccpPacketsRedir_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,5),_DeviceWccpPacketsRedir_Type())
deviceWccpPacketsRedir.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpPacketsRedir.setStatus(_A)
_DeviceWccpPacketsLowRedir_Type=Counter32
_DeviceWccpPacketsLowRedir_Object=MibTableColumn
deviceWccpPacketsLowRedir=_DeviceWccpPacketsLowRedir_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,6),_DeviceWccpPacketsLowRedir_Type())
deviceWccpPacketsLowRedir.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpPacketsLowRedir.setStatus(_A)
_DeviceWccpBytesRedir_Type=Counter64
_DeviceWccpBytesRedir_Object=MibTableColumn
deviceWccpBytesRedir=_DeviceWccpBytesRedir_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,7),_DeviceWccpBytesRedir_Type())
deviceWccpBytesRedir.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpBytesRedir.setStatus(_A)
if mibBuilder.loadTexts:deviceWccpBytesRedir.setUnits('Bytes')
_DeviceWccpBytesLowRedir_Type=Counter32
_DeviceWccpBytesLowRedir_Object=MibTableColumn
deviceWccpBytesLowRedir=_DeviceWccpBytesLowRedir_Object((1,3,6,1,4,1,3417,2,5,2,1,1,1,8),_DeviceWccpBytesLowRedir_Type())
deviceWccpBytesLowRedir.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceWccpBytesLowRedir.setStatus(_A)
if mibBuilder.loadTexts:deviceWccpBytesLowRedir.setUnits('Bytes')
mibBuilder.exportSymbols(_E,**{'WccpServiceType':WccpServiceType,'WccpVersion':WccpVersion,'deviceWccpMIB':deviceWccpMIB,'deviceWccpEnabled':deviceWccpEnabled,'deviceWccpMIBObjects':deviceWccpMIBObjects,'deviceWccpValues':deviceWccpValues,'deviceWccpValueTable':deviceWccpValueTable,'deviceWccpValueEntry':deviceWccpValueEntry,_F:deviceWccpIndex,'deviceWccpServiceID':deviceWccpServiceID,'deviceWccpServiceType':deviceWccpServiceType,'deviceWccpServiceVersion':deviceWccpServiceVersion,'deviceWccpPacketsRedir':deviceWccpPacketsRedir,'deviceWccpPacketsLowRedir':deviceWccpPacketsLowRedir,'deviceWccpBytesRedir':deviceWccpBytesRedir,'deviceWccpBytesLowRedir':deviceWccpBytesLowRedir})