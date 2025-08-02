_E='DisplayString'
_D='NotificationType'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols('CPQHOST-MIB','compaq','cpqHoTrapFlags')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_CpqApplianceMgmt_ObjectIdentity=ObjectIdentity
cpqApplianceMgmt=_CpqApplianceMgmt_ObjectIdentity((1,3,6,1,4,1,232,21))
_CpqApMibRev_ObjectIdentity=ObjectIdentity
cpqApMibRev=_CpqApMibRev_ObjectIdentity((1,3,6,1,4,1,232,21,1))
class _CpqApMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqApMibRevMajor_Type.__name__=_B
_CpqApMibRevMajor_Object=MibScalar
cpqApMibRevMajor=_CpqApMibRevMajor_Object((1,3,6,1,4,1,232,21,1,1),_CpqApMibRevMajor_Type())
cpqApMibRevMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqApMibRevMajor.setStatus(_A)
class _CpqApMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqApMibRevMinor_Type.__name__=_B
_CpqApMibRevMinor_Object=MibScalar
cpqApMibRevMinor=_CpqApMibRevMinor_Object((1,3,6,1,4,1,232,21,1,2),_CpqApMibRevMinor_Type())
cpqApMibRevMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqApMibRevMinor.setStatus(_A)
class _CpqApMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_CpqApMibCondition_Type.__name__=_B
_CpqApMibCondition_Object=MibScalar
cpqApMibCondition=_CpqApMibCondition_Object((1,3,6,1,4,1,232,21,1,3),_CpqApMibCondition_Type())
cpqApMibCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqApMibCondition.setStatus(_A)
_CpqApComponent_ObjectIdentity=ObjectIdentity
cpqApComponent=_CpqApComponent_ObjectIdentity((1,3,6,1,4,1,232,21,2))
_CpqApInterface_ObjectIdentity=ObjectIdentity
cpqApInterface=_CpqApInterface_ObjectIdentity((1,3,6,1,4,1,232,21,2,1))
_CpqApOsCommon_ObjectIdentity=ObjectIdentity
cpqApOsCommon=_CpqApOsCommon_ObjectIdentity((1,3,6,1,4,1,232,21,2,1,4))
class _CpqApOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqApOsCommonPollFreq_Type.__name__=_B
_CpqApOsCommonPollFreq_Object=MibScalar
cpqApOsCommonPollFreq=_CpqApOsCommonPollFreq_Object((1,3,6,1,4,1,232,21,2,1,4,1),_CpqApOsCommonPollFreq_Type())
cpqApOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqApOsCommonPollFreq.setStatus(_A)
_CpqApConfig_ObjectIdentity=ObjectIdentity
cpqApConfig=_CpqApConfig_ObjectIdentity((1,3,6,1,4,1,232,21,2,2))
_CpqApApplianceId_Type=Integer32
_CpqApApplianceId_Object=MibScalar
cpqApApplianceId=_CpqApApplianceId_Object((1,3,6,1,4,1,232,21,2,2,1),_CpqApApplianceId_Type())
cpqApApplianceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqApApplianceId.setStatus(_A)
class _CpqApApplianceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqApApplianceDescription_Type.__name__=_E
_CpqApApplianceDescription_Object=MibScalar
cpqApApplianceDescription=_CpqApApplianceDescription_Object((1,3,6,1,4,1,232,21,2,2,2),_CpqApApplianceDescription_Type())
cpqApApplianceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqApApplianceDescription.setStatus(_A)
mibBuilder.exportSymbols('CPQAPPLIANCE-MIB',**{'cpqApplianceMgmt':cpqApplianceMgmt,'cpqApMibRev':cpqApMibRev,'cpqApMibRevMajor':cpqApMibRevMajor,'cpqApMibRevMinor':cpqApMibRevMinor,'cpqApMibCondition':cpqApMibCondition,'cpqApComponent':cpqApComponent,'cpqApInterface':cpqApInterface,'cpqApOsCommon':cpqApOsCommon,'cpqApOsCommonPollFreq':cpqApOsCommonPollFreq,'cpqApConfig':cpqApConfig,'cpqApApplianceId':cpqApApplianceId,'cpqApApplianceDescription':cpqApApplianceDescription})