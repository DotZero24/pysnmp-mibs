_L='h323ExperimentalGroupVer1'
_K='h323AcceleratedRequestedLogicalChannel'
_J='h323AliasTypeRestriction'
_I='h323VoiceIfCodecG729Enable'
_H='h323UseEvenT38Port'
_G='h323AddT38MediaControlChannel'
_F='h323RegAsGateway'
_E='2005-03-25 00:00'
_D='read-write'
_C='MxEnableState'
_B='MX-H323-EXPERIMENTAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,MxIpHostName=mibBuilder.importSymbols('MX-TC',_C,'MxIpHostName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h323ExperimentalMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,60))
if mibBuilder.loadTexts:h323ExperimentalMIB.setRevisions(('2007-04-06 00:00',_E,_E,'2004-10-04 00:00','2004-08-03 00:00','2003-10-20 00:00','2003-10-06 00:00'))
_H323ExperimentalMIBObjects_ObjectIdentity=ObjectIdentity
h323ExperimentalMIBObjects=_H323ExperimentalMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,60,1))
_H323Interop_ObjectIdentity=ObjectIdentity
h323Interop=_H323Interop_ObjectIdentity((1,3,6,1,4,1,4935,99,60,1,5))
class _H323RegAsGateway_Type(MxEnableState):defaultValue=0
_H323RegAsGateway_Type.__name__=_C
_H323RegAsGateway_Object=MibScalar
h323RegAsGateway=_H323RegAsGateway_Object((1,3,6,1,4,1,4935,99,60,1,5,5),_H323RegAsGateway_Type())
h323RegAsGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:h323RegAsGateway.setStatus(_A)
class _H323AliasTypeRestriction_Type(MxEnableState):defaultValue=1
_H323AliasTypeRestriction_Type.__name__=_C
_H323AliasTypeRestriction_Object=MibScalar
h323AliasTypeRestriction=_H323AliasTypeRestriction_Object((1,3,6,1,4,1,4935,99,60,1,5,15),_H323AliasTypeRestriction_Type())
h323AliasTypeRestriction.setMaxAccess(_D)
if mibBuilder.loadTexts:h323AliasTypeRestriction.setStatus(_A)
class _H323AcceleratedRequestedLogicalChannel_Type(MxEnableState):defaultValue=0
_H323AcceleratedRequestedLogicalChannel_Type.__name__=_C
_H323AcceleratedRequestedLogicalChannel_Object=MibScalar
h323AcceleratedRequestedLogicalChannel=_H323AcceleratedRequestedLogicalChannel_Object((1,3,6,1,4,1,4935,99,60,1,5,18),_H323AcceleratedRequestedLogicalChannel_Type())
h323AcceleratedRequestedLogicalChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:h323AcceleratedRequestedLogicalChannel.setStatus(_A)
_H323VoiceIfCodecTable_Object=MibTable
h323VoiceIfCodecTable=_H323VoiceIfCodecTable_Object((1,3,6,1,4,1,4935,99,60,1,5,20))
if mibBuilder.loadTexts:h323VoiceIfCodecTable.setStatus(_A)
_H323VoiceIfCodecEntry_Object=MibTableRow
h323VoiceIfCodecEntry=_H323VoiceIfCodecEntry_Object((1,3,6,1,4,1,4935,99,60,1,5,20,1))
h323VoiceIfCodecEntry.setIndexNames((0,_B,'ifIndex'))
if mibBuilder.loadTexts:h323VoiceIfCodecEntry.setStatus(_A)
class _H323VoiceIfCodecG729Enable_Type(MxEnableState):defaultValue=0
_H323VoiceIfCodecG729Enable_Type.__name__=_C
_H323VoiceIfCodecG729Enable_Object=MibTableColumn
h323VoiceIfCodecG729Enable=_H323VoiceIfCodecG729Enable_Object((1,3,6,1,4,1,4935,99,60,1,5,20,1,5),_H323VoiceIfCodecG729Enable_Type())
h323VoiceIfCodecG729Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:h323VoiceIfCodecG729Enable.setStatus(_A)
class _H323AddT38MediaControlChannel_Type(MxEnableState):defaultValue=0
_H323AddT38MediaControlChannel_Type.__name__=_C
_H323AddT38MediaControlChannel_Object=MibScalar
h323AddT38MediaControlChannel=_H323AddT38MediaControlChannel_Object((1,3,6,1,4,1,4935,99,60,1,5,50),_H323AddT38MediaControlChannel_Type())
h323AddT38MediaControlChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:h323AddT38MediaControlChannel.setStatus(_A)
class _H323UseEvenT38Port_Type(MxEnableState):defaultValue=0
_H323UseEvenT38Port_Type.__name__=_C
_H323UseEvenT38Port_Object=MibScalar
h323UseEvenT38Port=_H323UseEvenT38Port_Object((1,3,6,1,4,1,4935,99,60,1,5,100),_H323UseEvenT38Port_Type())
h323UseEvenT38Port.setMaxAccess(_D)
if mibBuilder.loadTexts:h323UseEvenT38Port.setStatus(_A)
_H323ExperimentalConformance_ObjectIdentity=ObjectIdentity
h323ExperimentalConformance=_H323ExperimentalConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,60,2))
_H323ExperimentalCompliances_ObjectIdentity=ObjectIdentity
h323ExperimentalCompliances=_H323ExperimentalCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,60,2,1))
_H323ExperimentalGroups_ObjectIdentity=ObjectIdentity
h323ExperimentalGroups=_H323ExperimentalGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,60,2,2))
h323ExperimentalGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,60,2,2,5))
h323ExperimentalGroupVer1.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:h323ExperimentalGroupVer1.setStatus(_A)
h323ExperimentalBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,60,2,1,5))
h323ExperimentalBasicComplVer1.setObjects((_B,_L))
if mibBuilder.loadTexts:h323ExperimentalBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h323ExperimentalMIB':h323ExperimentalMIB,'h323ExperimentalMIBObjects':h323ExperimentalMIBObjects,'h323Interop':h323Interop,_F:h323RegAsGateway,_J:h323AliasTypeRestriction,_K:h323AcceleratedRequestedLogicalChannel,'h323VoiceIfCodecTable':h323VoiceIfCodecTable,'h323VoiceIfCodecEntry':h323VoiceIfCodecEntry,_I:h323VoiceIfCodecG729Enable,_G:h323AddT38MediaControlChannel,_H:h323UseEvenT38Port,'h323ExperimentalConformance':h323ExperimentalConformance,'h323ExperimentalCompliances':h323ExperimentalCompliances,'h323ExperimentalBasicComplVer1':h323ExperimentalBasicComplVer1,'h323ExperimentalGroups':h323ExperimentalGroups,_L:h323ExperimentalGroupVer1})