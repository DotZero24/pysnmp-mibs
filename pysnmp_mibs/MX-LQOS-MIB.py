_J='serviceClassesId'
_I='ethernet8021QTaggingInterfaceName'
_H='MxEnableState'
_G='OctetString'
_F='MX-LQOS-MIB'
_E='Integer32'
_D='read-only'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_H,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lQosMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2500))
_LQosMIBObjects_ObjectIdentity=ObjectIdentity
lQosMIBObjects=_LQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2500,1))
class _DefaultDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DefaultDiffServ_Type.__name__=_C
_DefaultDiffServ_Object=MibScalar
defaultDiffServ=_DefaultDiffServ_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,100),_DefaultDiffServ_Type())
defaultDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDiffServ.setStatus(_A)
class _DefaultTrafficClass_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DefaultTrafficClass_Type.__name__=_C
_DefaultTrafficClass_Object=MibScalar
defaultTrafficClass=_DefaultTrafficClass_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,150),_DefaultTrafficClass_Type())
defaultTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultTrafficClass.setStatus(_A)
_Ethernet8021QTaggingTable_Object=MibTable
ethernet8021QTaggingTable=_Ethernet8021QTaggingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,200))
if mibBuilder.loadTexts:ethernet8021QTaggingTable.setStatus(_A)
_Ethernet8021QTaggingEntry_Object=MibTableRow
ethernet8021QTaggingEntry=_Ethernet8021QTaggingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,200,1))
ethernet8021QTaggingEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:ethernet8021QTaggingEntry.setStatus(_A)
_Ethernet8021QTaggingInterfaceName_Type=OctetString
_Ethernet8021QTaggingInterfaceName_Object=MibTableColumn
ethernet8021QTaggingInterfaceName=_Ethernet8021QTaggingInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,200,1,100),_Ethernet8021QTaggingInterfaceName_Type())
ethernet8021QTaggingInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:ethernet8021QTaggingInterfaceName.setStatus(_A)
class _Ethernet8021QTaggingEnablePriorityTagging_Type(MxEnableState):defaultValue=0
_Ethernet8021QTaggingEnablePriorityTagging_Type.__name__=_H
_Ethernet8021QTaggingEnablePriorityTagging_Object=MibTableColumn
ethernet8021QTaggingEnablePriorityTagging=_Ethernet8021QTaggingEnablePriorityTagging_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,200,1,200),_Ethernet8021QTaggingEnablePriorityTagging_Type())
ethernet8021QTaggingEnablePriorityTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernet8021QTaggingEnablePriorityTagging.setStatus(_A)
class _Ethernet8021QTaggingDefaultUserPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Ethernet8021QTaggingDefaultUserPriority_Type.__name__=_C
_Ethernet8021QTaggingDefaultUserPriority_Object=MibTableColumn
ethernet8021QTaggingDefaultUserPriority=_Ethernet8021QTaggingDefaultUserPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,200,1,300),_Ethernet8021QTaggingDefaultUserPriority_Type())
ethernet8021QTaggingDefaultUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernet8021QTaggingDefaultUserPriority.setStatus(_A)
_ServiceClassesTable_Object=MibTable
serviceClassesTable=_ServiceClassesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300))
if mibBuilder.loadTexts:serviceClassesTable.setStatus(_A)
_ServiceClassesEntry_Object=MibTableRow
serviceClassesEntry=_ServiceClassesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1))
serviceClassesEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:serviceClassesEntry.setStatus(_A)
_ServiceClassesId_Type=Unsigned32
_ServiceClassesId_Object=MibTableColumn
serviceClassesId=_ServiceClassesId_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1,100),_ServiceClassesId_Type())
serviceClassesId.setMaxAccess(_D)
if mibBuilder.loadTexts:serviceClassesId.setStatus(_A)
class _ServiceClassesDescription_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ServiceClassesDescription_Type.__name__=_G
_ServiceClassesDescription_Object=MibTableColumn
serviceClassesDescription=_ServiceClassesDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1,200),_ServiceClassesDescription_Type())
serviceClassesDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:serviceClassesDescription.setStatus(_A)
class _ServiceClassesDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ServiceClassesDiffServ_Type.__name__=_C
_ServiceClassesDiffServ_Object=MibTableColumn
serviceClassesDiffServ=_ServiceClassesDiffServ_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1,300),_ServiceClassesDiffServ_Type())
serviceClassesDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceClassesDiffServ.setStatus(_A)
class _ServiceClassesTrafficClass_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ServiceClassesTrafficClass_Type.__name__=_C
_ServiceClassesTrafficClass_Object=MibTableColumn
serviceClassesTrafficClass=_ServiceClassesTrafficClass_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1,350),_ServiceClassesTrafficClass_Type())
serviceClassesTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceClassesTrafficClass.setStatus(_A)
class _ServiceClassesUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ServiceClassesUserPriority_Type.__name__=_C
_ServiceClassesUserPriority_Object=MibTableColumn
serviceClassesUserPriority=_ServiceClassesUserPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,300,1,400),_ServiceClassesUserPriority_Type())
serviceClassesUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:serviceClassesUserPriority.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_E
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_E
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2500,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'lQosMIB':lQosMIB,'lQosMIBObjects':lQosMIBObjects,'defaultDiffServ':defaultDiffServ,'defaultTrafficClass':defaultTrafficClass,'ethernet8021QTaggingTable':ethernet8021QTaggingTable,'ethernet8021QTaggingEntry':ethernet8021QTaggingEntry,_I:ethernet8021QTaggingInterfaceName,'ethernet8021QTaggingEnablePriorityTagging':ethernet8021QTaggingEnablePriorityTagging,'ethernet8021QTaggingDefaultUserPriority':ethernet8021QTaggingDefaultUserPriority,'serviceClassesTable':serviceClassesTable,'serviceClassesEntry':serviceClassesEntry,_J:serviceClassesId,'serviceClassesDescription':serviceClassesDescription,'serviceClassesDiffServ':serviceClassesDiffServ,'serviceClassesTrafficClass':serviceClassesTrafficClass,'serviceClassesUserPriority':serviceClassesUserPriority,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})