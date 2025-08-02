_G='atiswitchEnhStackSwId'
_F='AtiStackInfo-MIB'
_E='read-write'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
alliedTelesyn=ModuleIdentity((1,3,6,1,4,1,207))
class MACAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_MibObject_ObjectIdentity=ObjectIdentity
mibObject=_MibObject_ObjectIdentity((1,3,6,1,4,1,207,8))
_AtiStackInfoMib_ObjectIdentity=ObjectIdentity
atiStackInfoMib=_AtiStackInfoMib_ObjectIdentity((1,3,6,1,4,1,207,8,16))
_AtiswitchEnhancedStacking_ObjectIdentity=ObjectIdentity
atiswitchEnhancedStacking=_AtiswitchEnhancedStacking_ObjectIdentity((1,3,6,1,4,1,207,8,16,1))
class _AtiswitchEnhStackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('unavailable',3)))
_AtiswitchEnhStackMode_Type.__name__=_D
_AtiswitchEnhStackMode_Object=MibScalar
atiswitchEnhStackMode=_AtiswitchEnhStackMode_Object((1,3,6,1,4,1,207,8,16,1,1),_AtiswitchEnhStackMode_Type())
atiswitchEnhStackMode.setMaxAccess(_E)
if mibBuilder.loadTexts:atiswitchEnhStackMode.setStatus(_A)
class _AtiswitchEnhStackDiscover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discover',1),('do-not-discover',2)))
_AtiswitchEnhStackDiscover_Type.__name__=_D
_AtiswitchEnhStackDiscover_Object=MibScalar
atiswitchEnhStackDiscover=_AtiswitchEnhStackDiscover_Object((1,3,6,1,4,1,207,8,16,1,2),_AtiswitchEnhStackDiscover_Type())
atiswitchEnhStackDiscover.setMaxAccess(_E)
if mibBuilder.loadTexts:atiswitchEnhStackDiscover.setStatus(_A)
_AtiswitchEnhStackRemoteNumber_Type=Integer32
_AtiswitchEnhStackRemoteNumber_Object=MibScalar
atiswitchEnhStackRemoteNumber=_AtiswitchEnhStackRemoteNumber_Object((1,3,6,1,4,1,207,8,16,1,3),_AtiswitchEnhStackRemoteNumber_Type())
atiswitchEnhStackRemoteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackRemoteNumber.setStatus(_A)
_AtiswitchEnhStackTable_Object=MibTable
atiswitchEnhStackTable=_AtiswitchEnhStackTable_Object((1,3,6,1,4,1,207,8,16,1,4))
if mibBuilder.loadTexts:atiswitchEnhStackTable.setStatus(_A)
_AtiswitchEnhStackEntry_Object=MibTableRow
atiswitchEnhStackEntry=_AtiswitchEnhStackEntry_Object((1,3,6,1,4,1,207,8,16,1,4,1))
atiswitchEnhStackEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:atiswitchEnhStackEntry.setStatus(_A)
class _AtiswitchEnhStackSwId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiswitchEnhStackSwId_Type.__name__=_D
_AtiswitchEnhStackSwId_Object=MibTableColumn
atiswitchEnhStackSwId=_AtiswitchEnhStackSwId_Object((1,3,6,1,4,1,207,8,16,1,4,1,1),_AtiswitchEnhStackSwId_Type())
atiswitchEnhStackSwId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwId.setStatus(_A)
_AtiswitchEnhStackSwMacAddr_Type=MACAddress
_AtiswitchEnhStackSwMacAddr_Object=MibTableColumn
atiswitchEnhStackSwMacAddr=_AtiswitchEnhStackSwMacAddr_Object((1,3,6,1,4,1,207,8,16,1,4,1,2),_AtiswitchEnhStackSwMacAddr_Type())
atiswitchEnhStackSwMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwMacAddr.setStatus(_A)
class _AtiswitchEnhStackSwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchEnhStackSwName_Type.__name__=_C
_AtiswitchEnhStackSwName_Object=MibTableColumn
atiswitchEnhStackSwName=_AtiswitchEnhStackSwName_Object((1,3,6,1,4,1,207,8,16,1,4,1,3),_AtiswitchEnhStackSwName_Type())
atiswitchEnhStackSwName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwName.setStatus(_A)
class _AtiswitchEnhStackSwMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchEnhStackSwMode_Type.__name__=_C
_AtiswitchEnhStackSwMode_Object=MibTableColumn
atiswitchEnhStackSwMode=_AtiswitchEnhStackSwMode_Object((1,3,6,1,4,1,207,8,16,1,4,1,4),_AtiswitchEnhStackSwMode_Type())
atiswitchEnhStackSwMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwMode.setStatus(_A)
class _AtiswitchEnhStackSwSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchEnhStackSwSoftwareVersion_Type.__name__=_C
_AtiswitchEnhStackSwSoftwareVersion_Object=MibTableColumn
atiswitchEnhStackSwSoftwareVersion=_AtiswitchEnhStackSwSoftwareVersion_Object((1,3,6,1,4,1,207,8,16,1,4,1,5),_AtiswitchEnhStackSwSoftwareVersion_Type())
atiswitchEnhStackSwSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwSoftwareVersion.setStatus(_A)
class _AtiswitchEnhStackSwModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtiswitchEnhStackSwModel_Type.__name__=_C
_AtiswitchEnhStackSwModel_Object=MibTableColumn
atiswitchEnhStackSwModel=_AtiswitchEnhStackSwModel_Object((1,3,6,1,4,1,207,8,16,1,4,1,6),_AtiswitchEnhStackSwModel_Type())
atiswitchEnhStackSwModel.setMaxAccess(_B)
if mibBuilder.loadTexts:atiswitchEnhStackSwModel.setStatus(_A)
_AtiswitchEnhStackConnect_Type=TruthValue
_AtiswitchEnhStackConnect_Object=MibTableColumn
atiswitchEnhStackConnect=_AtiswitchEnhStackConnect_Object((1,3,6,1,4,1,207,8,16,1,4,1,7),_AtiswitchEnhStackConnect_Type())
atiswitchEnhStackConnect.setMaxAccess(_E)
if mibBuilder.loadTexts:atiswitchEnhStackConnect.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'MACAddress':MACAddress,'alliedTelesyn':alliedTelesyn,'mibObject':mibObject,'atiStackInfoMib':atiStackInfoMib,'atiswitchEnhancedStacking':atiswitchEnhancedStacking,'atiswitchEnhStackMode':atiswitchEnhStackMode,'atiswitchEnhStackDiscover':atiswitchEnhStackDiscover,'atiswitchEnhStackRemoteNumber':atiswitchEnhStackRemoteNumber,'atiswitchEnhStackTable':atiswitchEnhStackTable,'atiswitchEnhStackEntry':atiswitchEnhStackEntry,_G:atiswitchEnhStackSwId,'atiswitchEnhStackSwMacAddr':atiswitchEnhStackSwMacAddr,'atiswitchEnhStackSwName':atiswitchEnhStackSwName,'atiswitchEnhStackSwMode':atiswitchEnhStackSwMode,'atiswitchEnhStackSwSoftwareVersion':atiswitchEnhStackSwSoftwareVersion,'atiswitchEnhStackSwModel':atiswitchEnhStackSwModel,'atiswitchEnhStackConnect':atiswitchEnhStackConnect})